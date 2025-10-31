import os
import streamlit as st
from google import genai
from google.genai import types

# IMPORTANT: KEEP THIS COMMENT
# Follow these instructions when using this blueprint:
# - Note that the newest Gemini model series is "gemini-2.5-flash" or gemini-2.5-pro"
#   - Using gemini-2.5-pro as requested by user
# - The SDK was recently renamed from google-generativeai to google-genai

# This API key is from Gemini Developer API Key, not vertex AI API Key
def get_client():
    """Get or create Gemini client with API key validation.
    
    Checks Streamlit secrets first, then environment variables.
    """
    api_key = None
    
    # Prefer Streamlit secrets for deployment safety
    if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
    else:
        api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found. Please add it to .streamlit/secrets.toml "
            "or set it as an environment variable."
        )
    return genai.Client(api_key=api_key)


def generate_meal_plan(goal: str, ingredients: str, dietary_preferences: str = "") -> str:
    """
    Generate a weekly meal plan based on fitness goal and available ingredients.
    
    Args:
        goal: Fitness goal (weight loss, weight gain, or maintenance)
        ingredients: List of available pantry ingredients
        dietary_preferences: Any dietary restrictions or preferences
        
    Returns:
        A formatted weekly meal plan as a string
    """
    prompt = f"""You are a professional nutritionist and meal planner. Create a detailed 7-day meal plan based on the following:

GOAL: {goal}
AVAILABLE INGREDIENTS: {ingredients}
{f'DIETARY PREFERENCES: {dietary_preferences}' if dietary_preferences else ''}

Please provide a comprehensive weekly meal plan with the following structure for EACH DAY (Day 1 through Day 7):

**Day X:**
- **Breakfast:** [Meal name] - [Brief description, calories, protein in grams]
- **Lunch:** [Meal name] - [Brief description, calories, protein in grams]
- **Dinner:** [Meal name] - [Brief description, calories, protein in grams]
- **Snacks:** [Snack items] - [Brief description, calories, protein in grams]
- **Daily Total:** [Total calories] calories, [Total protein]g protein

Guidelines:
1. For WEIGHT LOSS: Focus on calorie deficit (1500-1800 calories/day), high protein (100-120g), moderate carbs
2. For WEIGHT GAIN: Focus on calorie surplus (2500-3000 calories/day), high protein (140-180g), balanced macros
3. For MAINTENANCE: Balanced nutrition (2000-2200 calories/day), adequate protein (100-130g)
4. Use ONLY the ingredients provided or common staples (salt, pepper, oil, water)
5. Ensure variety across the week
6. Include realistic portion sizes and simple recipes
7. Make meals practical and easy to prepare

Provide the meal plan in a clear, organized format."""

    try:
        client = get_client()
        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )
        return response.text or "Unable to generate meal plan. Please try again."
    except Exception as e:
        return f"Error generating meal plan: {str(e)}"


def generate_exercise_plan(goal: str, equipment: str, fitness_level: str = "intermediate") -> str:
    """
    Generate a weekly exercise plan based on fitness goal and available equipment.
    
    Args:
        goal: Fitness goal (weight loss, weight gain, or maintenance)
        equipment: List of available exercise equipment
        fitness_level: User's fitness level (beginner, intermediate, advanced)
        
    Returns:
        A formatted weekly exercise plan as a string
    """
    prompt = f"""You are a certified personal trainer. Create a detailed 7-day workout plan based on the following:

GOAL: {goal}
AVAILABLE EQUIPMENT: {equipment}
FITNESS LEVEL: {fitness_level}

Please provide a comprehensive weekly exercise plan with the following structure for EACH DAY (Day 1 through Day 7):

**Day X: [Workout Type]**
- **Focus:** [Muscle group or cardio type]
- **Duration:** [Total workout time]
- **Exercises:**
  1. [Exercise name] - [Sets] sets x [Reps] reps - [Rest time between sets]
  2. [Exercise name] - [Sets] sets x [Reps] reps - [Rest time between sets]
  3. [Continue for all exercises]
- **Cooldown:** [Stretching/cooldown routine]
- **Notes:** [Any important tips or modifications]

Guidelines:
1. For WEIGHT LOSS: Focus on cardio, HIIT, circuit training (5-6 days/week), higher reps (12-15)
2. For WEIGHT GAIN: Focus on strength training, muscle building (4-5 days/week), lower reps (6-10), progressive overload
3. For MAINTENANCE: Balanced mix of cardio and strength (4-5 days/week), moderate intensity
4. Use ONLY the equipment provided or bodyweight exercises
5. Include proper rest days (1-2 per week)
6. Provide warm-up recommendations
7. Include exercise progressions and modifications
8. Ensure balanced muscle group coverage throughout the week

Provide the exercise plan in a clear, organized format with specific sets, reps, and rest periods."""

    try:
        client = get_client()
        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )
        return response.text or "Unable to generate exercise plan. Please try again."
    except Exception as e:
        return f"Error generating exercise plan: {str(e)}"
