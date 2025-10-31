import streamlit as st
from datetime import datetime
from auth import delete_plan

def show_history_page():
    """Display user's plan history."""
    st.title("📊 Your Plan History")
    st.markdown("View and manage all your previously generated meal and exercise plans")
    
    st.markdown("---")
    
    if not st.session_state.plan_history:
        st.info("🌟 No plans yet! Head to the Planner page to create your first plan.")
        if st.button("🚀 Create Your First Plan", type="primary"):
            st.session_state.current_page = 'planner'
            st.rerun()
        return
    
    filter_type = st.selectbox(
        "Filter by type:",
        ["All", "Meal Plans", "Exercise Plans"]
    )
    
    st.markdown(f"### Total Plans: {len(st.session_state.plan_history)}")
    st.markdown("---")
    
    filtered_plans = st.session_state.plan_history
    if filter_type == "Meal Plans":
        filtered_plans = [p for p in st.session_state.plan_history if p['type'] == 'meal']
    elif filter_type == "Exercise Plans":
        filtered_plans = [p for p in st.session_state.plan_history if p['type'] == 'exercise']
    
    for idx, plan in enumerate(filtered_plans):
        created_date = datetime.fromisoformat(plan['created_at']).strftime("%B %d, %Y at %I:%M %p")
        
        plan_icon = "🍽️" if plan['type'] == 'meal' else "💪"
        plan_type_name = "Meal Plan" if plan['type'] == 'meal' else "Exercise Plan"
        
        with st.expander(f"{plan_icon} {plan_type_name} - {plan['goal']} ({created_date})", expanded=(idx == 0)):
            st.markdown(plan['content'])
            
            col1, col2 = st.columns([3, 1])
            with col2:
                if st.button(f"🗑️ Delete", key=f"delete_{plan.get('id', idx)}"):
                    pid = plan.get('id')
                    if pid:
                        delete_plan(pid)
                        st.success("Plan deleted!")
                        st.rerun()
    
    st.markdown("---")
    
    if st.button("🗑️ Clear All History", type="secondary"):
        if st.session_state.get('confirm_clear', False):
            # Bulk delete all user's plans
            from supabase_client import get_supabase
            if st.session_state.get('user_id'):
                get_supabase().table('plans').delete().eq('user_id', st.session_state.user_id).execute()
                st.session_state.plan_history = []
            st.session_state.confirm_clear = False
            st.success("All history cleared!")
            st.rerun()
        else:
            st.session_state.confirm_clear = True
            st.warning("⚠️ Click again to confirm deletion of all history")
