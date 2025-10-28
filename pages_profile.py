import streamlit as st
from auth import update_user_data, sign_out

def show_profile_page():
    """Display user profile and settings page."""
    st.title("⚙️ Profile & Settings")
    st.markdown("Manage your account and fitness preferences")
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("👤 Account Information")
        st.write(f"**Username:** {st.session_state.username}")
        st.write(f"**Email:** {st.session_state.user_data.get('email', 'N/A')}")
        st.write(f"**Member since:** {st.session_state.user_data.get('created_at', 'N/A')[:10]}")
    
    with col2:
        if st.button("🚪 Sign Out", type="secondary", use_container_width=True):
            sign_out()
            st.rerun()
    
    st.markdown("---")
    
    st.subheader("🎯 Fitness Goals & Preferences")
    
    with st.form("profile_form"):
        fitness_goal = st.selectbox(
            "Primary Fitness Goal",
            ["Weight Loss", "Weight Gain", "Maintenance"],
            index=["Weight Loss", "Weight Gain", "Maintenance"].index(
                st.session_state.user_data.get('fitness_goal', 'Maintenance')
            )
        )
        
        fitness_level = st.selectbox(
            "Fitness Level",
            ["Beginner", "Intermediate", "Advanced"],
            index=["Beginner", "Intermediate", "Advanced"].index(
                st.session_state.user_data.get('fitness_level', 'Intermediate')
            )
        )
        
        st.markdown("---")
        
        st.subheader("📝 Default Preferences (Optional)")
        st.caption("These will be pre-filled when creating new plans")
        
        default_ingredients = st.text_area(
            "Default Pantry Ingredients",
            value=st.session_state.user_data.get('default_ingredients', ''),
            placeholder="e.g., chicken, rice, eggs, broccoli...",
            height=100
        )
        
        default_equipment = st.text_area(
            "Default Exercise Equipment",
            value=st.session_state.user_data.get('default_equipment', ''),
            placeholder="e.g., dumbbells, resistance bands, yoga mat...",
            height=100
        )
        
        dietary_preferences = st.text_input(
            "Dietary Preferences/Restrictions",
            value=st.session_state.user_data.get('dietary_preferences', ''),
            placeholder="e.g., vegetarian, no dairy..."
        )
        
        st.markdown("---")
        
        submit = st.form_submit_button("💾 Save Changes", type="primary", use_container_width=True)
        
        if submit:
            updated_data = {
                'fitness_goal': fitness_goal,
                'fitness_level': fitness_level,
                'default_ingredients': default_ingredients,
                'default_equipment': default_equipment,
                'dietary_preferences': dietary_preferences
            }
            
            update_user_data(st.session_state.username, updated_data)
            st.success("✅ Profile updated successfully!")
            st.rerun()
    
    st.markdown("---")
    
    st.subheader("📊 Statistics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_plans = len(st.session_state.plan_history)
        st.metric("Total Plans", total_plans)
    
    with col2:
        meal_plans = len([p for p in st.session_state.plan_history if p['type'] == 'meal'])
        st.metric("Meal Plans", meal_plans)
    
    with col3:
        exercise_plans = len([p for p in st.session_state.plan_history if p['type'] == 'exercise'])
        st.metric("Exercise Plans", exercise_plans)
