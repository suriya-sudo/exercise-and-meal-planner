import streamlit as st
import json
import os
from datetime import datetime
from typing import Optional, Dict, Any

USERS_FILE = "users.json"

def load_users() -> Dict[str, Any]:
    """Load users from JSON file."""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_users(users: Dict[str, Any]) -> None:
    """Save users to JSON file."""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def init_session_state():
    """Initialize session state variables."""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {}
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'landing'
    if 'plan_history' not in st.session_state:
        st.session_state.plan_history = []

def sign_up(username: str, password: str, email: str) -> tuple[bool, str]:
    """Register a new user."""
    users = load_users()
    
    if not username or not password or not email:
        return False, "All fields are required"
    
    if username in users:
        return False, "Username already exists"
    
    users[username] = {
        'password': password,
        'email': email,
        'created_at': datetime.now().isoformat(),
        'fitness_goal': 'Maintenance',
        'fitness_level': 'Intermediate',
        'plan_history': []
    }
    
    save_users(users)
    return True, "Account created successfully!"

def sign_in(username: str, password: str) -> tuple[bool, str]:
    """Authenticate a user."""
    users = load_users()
    
    if username not in users:
        return False, "Username not found"
    
    if users[username]['password'] != password:
        return False, "Incorrect password"
    
    st.session_state.authenticated = True
    st.session_state.username = username
    st.session_state.user_data = users[username]
    st.session_state.plan_history = users[username].get('plan_history', [])
    
    return True, "Successfully logged in!"

def sign_out():
    """Sign out the current user."""
    st.session_state.authenticated = False
    st.session_state.username = None
    st.session_state.user_data = {}
    st.session_state.plan_history = []
    st.session_state.current_page = 'landing'

def update_user_data(username: str, data: Dict[str, Any]) -> None:
    """Update user data in storage."""
    users = load_users()
    if username in users:
        users[username].update(data)
        save_users(users)
        st.session_state.user_data = users[username]

def add_plan_to_history(plan_type: str, plan_content: str, goal: str) -> None:
    """Add a generated plan to user's history."""
    if not st.session_state.authenticated:
        return
    
    plan_entry = {
        'type': plan_type,
        'content': plan_content,
        'goal': goal,
        'created_at': datetime.now().isoformat()
    }
    
    st.session_state.plan_history.insert(0, plan_entry)
    
    users = load_users()
    username = st.session_state.username
    if username in users:
        if 'plan_history' not in users[username]:
            users[username]['plan_history'] = []
        users[username]['plan_history'].insert(0, plan_entry)
        users[username]['plan_history'] = users[username]['plan_history'][:20]
        save_users(users)

def show_auth_page():
    """Display authentication page with sign in/sign up."""
    st.title("Welcome to Meal & Exercise Planner")
    
    tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
    
    with tab1:
        st.subheader("Sign In to Your Account")
        with st.form("signin_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Sign In", use_container_width=True)
            
            if submit:
                success, message = sign_in(username, password)
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
                        st.info("You can now sign in with your credentials")
                    else:
                        st.error(message)
    
    st.markdown("---")
    if st.button("← Back to Home"):
        st.session_state.current_page = 'landing'
        st.rerun()
