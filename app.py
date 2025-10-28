import streamlit as st
from auth import init_session_state, show_auth_page
from pages_landing import show_landing_page
from pages_planner import show_planner_page
from pages_history import show_history_page
from pages_profile import show_profile_page

st.set_page_config(
    page_title="Meal & Exercise Planner",
    page_icon="🏋️",
    layout="wide"
)

init_session_state()

def show_navigation():
    """Display navigation sidebar for authenticated users."""
    with st.sidebar:
        st.markdown(f"### 👋 Welcome, {st.session_state.username}!")
        st.markdown("---")
        
        if st.button("🏠 Home", use_container_width=True, type="primary" if st.session_state.current_page == 'planner' else "secondary"):
            st.session_state.current_page = 'planner'
            st.rerun()
        
        if st.button("📊 History", use_container_width=True, type="primary" if st.session_state.current_page == 'history' else "secondary"):
            st.session_state.current_page = 'history'
            st.rerun()
        
        if st.button("⚙️ Profile & Settings", use_container_width=True, type="primary" if st.session_state.current_page == 'profile' else "secondary"):
            st.session_state.current_page = 'profile'
            st.rerun()
        
        st.markdown("---")
        
        st.markdown("""
            <div style='text-align: center; color: gray; font-size: 0.85em; padding: 1rem;'>
            <p>🏋️ Meal & Exercise Planner</p>
            <p>Powered by Gemini AI</p>
            </div>
        """, unsafe_allow_html=True)

if st.session_state.current_page == 'landing':
    show_landing_page()

elif st.session_state.current_page == 'auth':
    show_auth_page()

elif st.session_state.authenticated:
    show_navigation()
    
    if st.session_state.current_page == 'planner':
        show_planner_page()
    
    elif st.session_state.current_page == 'history':
        show_history_page()
    
    elif st.session_state.current_page == 'profile':
        show_profile_page()

else:
    st.session_state.current_page = 'landing'
    st.rerun()
