import streamlit as st
from datetime import datetime
from typing import Optional, Dict, Any
from supabase_client import get_supabase

def init_session_state():
    """Initialize session state variables."""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {}
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'landing'
    if 'plan_history' not in st.session_state:
        st.session_state.plan_history = []

def _safe_data(res: Any) -> Any:
    """Return the 'data' field from a Supabase response regardless of shape."""
    if res is None:
        return None
    data = getattr(res, 'data', None)
    if data is None and isinstance(res, dict):
        data = res.get('data')
    return data

def _fetch_profile(user_id: str) -> Dict[str, Any]:
    sb = get_supabase()
    res = sb.table('profiles').select('*').eq('id', user_id).maybe_single().execute()
    data = _safe_data(res)
    return data or {}

def _ensure_profile(user_id: str, username: Optional[str], email: Optional[str]) -> Dict[str, Any]:
    sb = get_supabase()
    existing = _fetch_profile(user_id)
    if existing:
        return existing
    payload: Dict[str, Any] = {
        'id': user_id,
        'username': username or None,
        'email': email or None,
        'fitness_goal': 'Maintenance',
        'fitness_level': 'Intermediate',
        'created_at': datetime.now().isoformat(),
    }
    sb.table('profiles').insert(payload).execute()
    return payload

def _refresh_plan_history(user_id: str) -> None:
    sb = get_supabase()
    res = (
        sb.table('plans')
        .select('*')
        .eq('user_id', user_id)
        .order('created_at', desc=True)
        .limit(20)
        .execute()
    )
    data = _safe_data(res)
    st.session_state.plan_history = data or []

def sign_up(username: str, password: str, email: str) -> tuple[bool, str]:
    """Register a new user in Supabase Auth and create a profile."""
    if not username or not password or not email:
        return False, "All fields are required"

    sb = get_supabase()
    try:
        result = sb.auth.sign_up({
            'email': email,
            'password': password,
        })
        user = getattr(result, 'user', None)
        # Do NOT insert into profiles here due to RLS; we'll create it after sign-in
        if user:
            return True, "Account created. Please sign in to continue."
        else:
            return True, "Sign-up initiated. Please sign in to continue."
    except Exception as e:
        return False, f"Sign-up failed: {e}"

def sign_in(email: str, password: str) -> tuple[bool, str]:
    """Authenticate a user against Supabase Auth and load profile/history."""
    if not email or not password:
        return False, "Email and password are required"

    sb = get_supabase()
    try:
        session = sb.auth.sign_in_with_password({
            'email': email,
            'password': password,
        })
        user = getattr(session, 'user', None)
        if not user:
            return False, "Login failed"

        st.session_state.authenticated = True
        st.session_state.user_id = user.id
        profile = _ensure_profile(user.id, username=None, email=email)
        st.session_state.user_data = profile
        st.session_state.username = profile.get('username') or (email.split('@')[0] if email else None)
        _refresh_plan_history(user.id)
        return True, "Successfully logged in!"
    except Exception as e:
        return False, f"Login failed: {e}"

def sign_out():
    """Sign out the current user."""
    try:
        get_supabase().auth.sign_out()
    except Exception:
        pass
    st.session_state.authenticated = False
    st.session_state.username = None
    st.session_state.user_id = None
    st.session_state.user_data = {}
    st.session_state.plan_history = []
    st.session_state.current_page = 'landing'

def update_user_data(username: str, data: Dict[str, Any]) -> None:
    """Update user profile in Supabase and session state."""
    if not st.session_state.get('user_id'):
        return
    user_id: str = st.session_state.user_id
    sb = get_supabase()
    sb.table('profiles').update(data).eq('id', user_id).execute()
    st.session_state.user_data = {**st.session_state.user_data, **data}

def add_plan_to_history(plan_type: str, plan_content: str, goal: str) -> None:
    """Add a generated plan to user's history in Supabase."""
    if not st.session_state.get('authenticated') or not st.session_state.get('user_id'):
        return
    sb = get_supabase()
    plan_entry = {
        'user_id': st.session_state.user_id,
        'type': plan_type,
        'content': plan_content,
        'goal': goal,
        'created_at': datetime.now().isoformat()
    }
    sb.table('plans').insert(plan_entry).execute()
    _refresh_plan_history(st.session_state.user_id)

def delete_plan(plan_id: str) -> None:
    """Delete a plan by id and refresh local history."""
    if not st.session_state.get('user_id'):
        return
    sb = get_supabase()
    sb.table('plans').delete().eq('id', plan_id).eq('user_id', st.session_state.user_id).execute()
    _refresh_plan_history(st.session_state.user_id)

def show_auth_page():
    """Display authentication page with sign in/sign up."""
    st.title("Welcome to Meal & Exercise Planner")
    
    tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
    
    with tab1:
        st.subheader("Sign In to Your Account")
        with st.form("signin_form"):
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Sign In", use_container_width=True)
            
            if submit:
                success, message = sign_in(email, password)
                if success:
                    st.success(message)
                    st.session_state.current_page = 'planner'
                    st.rerun()
                else:
                    st.error(message)
    
    with tab2:
        st.subheader("Create a New Account")
        with st.form("signup_form"):
            new_username = st.text_input("Choose a Username")
            new_email = st.text_input("Email Address")
            new_password = st.text_input("Choose a Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submit_signup = st.form_submit_button("Sign Up", use_container_width=True)
            
            if submit_signup:
                if new_password != confirm_password:
                    st.error("Passwords do not match")
                else:
                    success, message = sign_up(new_username, new_password, new_email)
                    if success:
                        st.success(message)
                        st.info("If email confirmation is enabled, check your inbox to confirm before signing in.")
                    else:
                        st.error(message)
    
    st.markdown("---")
    if st.button("← Back to Home"):
        st.session_state.current_page = 'landing'
        st.rerun()
