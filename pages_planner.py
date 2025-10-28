import streamlit as st
from gemini import generate_meal_plan, generate_exercise_plan
from auth import add_plan_to_history

def show_planner_page():
    """Display the meal and exercise planner page."""
    st.title("🏋️ Create Your Weekly Plan")
    st.markdown("Generate personalized meal and exercise plans tailored to your goals!")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Your Fitness Goal")
        goal = st.selectbox(
            "What is your primary fitness goal?",
            ["Weight Loss", "Weight Gain", "Maintenance"],
            index=["Weight Loss", "Weight Gain", "Maintenance"].index(st.session_state.user_data.get('fitness_goal', 'Maintenance')),
            help="Select your current fitness objective"
        )
    
    with col2:
        st.subheader("💪 Fitness Level")
        fitness_level = st.selectbox(
            "What is your current fitness level?",
            ["Beginner", "Intermediate", "Advanced"],
            index=["Beginner", "Intermediate", "Advanced"].index(st.session_state.user_data.get('fitness_level', 'Intermediate')),
            help="This helps customize your exercise intensity"
        )
    
    st.markdown("---")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("🥗 Pantry Ingredients")
        ingredients = st.text_area(
            "List the ingredients you have available:",
            placeholder="e.g., chicken breast, rice, eggs, spinach, oats, bananas, almonds, olive oil, sweet potatoes, broccoli, salmon, quinoa, Greek yogurt, berries...",
            height=150,
            help="Enter ingredients separated by commas or on new lines"
        )
        
        dietary_preferences = st.text_input(
            "Dietary preferences or restrictions (optional):",
            placeholder="e.g., vegetarian, no dairy, low carb...",
            help="Any dietary restrictions or preferences"
        )
    
    with col4:
        st.subheader("🏋️ Exercise Equipment")
        equipment = st.text_area(
            "List the exercise equipment you have at home:",
            placeholder="e.g., dumbbells, resistance bands, yoga mat, pull-up bar, kettlebell, treadmill, bench...",
            height=150,
            help="Enter equipment separated by commas or on new lines. Include 'bodyweight' if you have no equipment."
        )
    
    st.markdown("---")
    
    if st.button("🚀 Generate My Weekly Plan", type="primary", use_container_width=True):
        if not ingredients.strip():
            st.error("⚠️ Please enter at least some ingredients from your pantry!")
        elif not equipment.strip():
            st.error("⚠️ Please enter your available exercise equipment (or 'bodyweight' if none)!")
        else:
            with st.spinner("🤖 AI is creating your personalized plans... This may take a moment."):
                tab1, tab2 = st.tabs(["🍽️ Meal Plan", "💪 Exercise Plan"])
                
                with tab1:
                    st.subheader(f"Your Weekly Meal Plan for {goal}")
                    meal_plan = generate_meal_plan(
                        goal=goal,
                        ingredients=ingredients,
                        dietary_preferences=dietary_preferences
                    )
                    st.markdown(meal_plan)
                    add_plan_to_history("meal", meal_plan, goal)
                    st.success("✅ Meal plan generated successfully!")
                
                with tab2:
                    st.subheader(f"Your Weekly Exercise Plan for {goal}")
                    exercise_plan = generate_exercise_plan(
                        goal=goal,
                        equipment=equipment,
                        fitness_level=fitness_level.lower()
                    )
                    st.markdown(exercise_plan)
                    add_plan_to_history("exercise", exercise_plan, goal)
                    st.success("✅ Exercise plan generated successfully!")
            
            st.balloons()
            
            st.markdown("---")
            st.info("💡 **Tips:** Your plans are saved in your history. Check the History page to view all your previous plans!")
