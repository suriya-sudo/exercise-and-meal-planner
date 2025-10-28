# 🏋️ AI-Powered Meal & Exercise Planner

A personalized fitness planning application that uses Google's Gemini AI to generate customized weekly meal and exercise plans based on your fitness goals, available ingredients, and home equipment.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Gemini-AI-4285F4?style=for-the-badge&logo=google&logoColor=white)

## ✨ Features

### Core Functionality
- 🎯 **Personalized Goal Setting** - Choose between weight loss, weight gain, or maintenance
- 🍽️ **AI-Generated Meal Plans** - Weekly meal plans based on your pantry ingredients
- 💪 **Custom Workout Routines** - Exercise plans tailored to your available equipment and fitness level
- 📊 **Detailed Nutrition Info** - Calorie counts and macronutrient breakdowns for each meal
- 🏃 **Exercise Specifications** - Complete workout details with sets, reps, and rest periods

### User Features
- 🔐 **User Authentication** - Sign up and sign in to save your plans
- 📈 **Plan History** - View and manage all your previously generated plans
- ⚙️ **Profile Management** - Edit your fitness goals and save default preferences
- 🎨 **Modern UI** - Clean, responsive interface with intuitive navigation

## 🚀 Quick Start

### Option 1: Run on Replit (Easiest)

1. Fork this repository on Replit
2. Add your `GEMINI_API_KEY` to Replit Secrets (see [Getting API Key](#getting-gemini-api-key))
3. Click "Run" - the app will start automatically!

### Option 2: Run Locally

#### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- A Gemini API key (free from Google)

#### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/meal-exercise-planner.git
   cd meal-exercise-planner
   ```

2. **Install dependencies**
   
   **Option A: Install core dependencies only (recommended for local use)**
   ```bash
   pip install streamlit google-genai
   ```
   
   **Option B: Install all dependencies (including Replit-specific packages)**
   ```bash
   pip install streamlit google-genai sift-stack-py
   ```
   
   Note: `sift-stack-py` is only needed when running on Replit.

3. **Set up your Gemini API key**
   
   **On Linux/Mac:**
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```
   
   **On Windows:**
   ```cmd
   set GEMINI_API_KEY=your-api-key-here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py --server.port 5000
   ```

5. **Open your browser**
   - Navigate to `http://localhost:5000`
   - Start creating your personalized fitness plans!

## 🔑 Getting Gemini API Key

The app uses Google's Gemini AI model (gemini-2.5-pro) to generate plans. Here's how to get your free API key:

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key
5. Add it to your environment (see installation steps above)

**Note:** The API has a free tier that's perfect for personal use!

## 📖 How to Use

### 1. **Sign Up / Sign In**
- Create a new account or sign in with existing credentials
- Your plans and preferences will be saved to your account

### 2. **Create Your Plan**
- **Set Your Goal:** Choose weight loss, weight gain, or maintenance
- **Enter Ingredients:** List what you have in your pantry
- **Add Equipment:** Specify your available exercise equipment
- **Generate:** Click the button and let AI create your personalized plans!

### 3. **View Your Plans**
- **Meal Plan Tab:** See 7 days of breakfast, lunch, dinner, and snacks
- **Exercise Plan Tab:** Get daily workout routines with specific exercises
- Plans are automatically saved to your history

### 4. **Manage Your Profile**
- Update your fitness goals anytime
- Save default ingredients and equipment for faster plan generation
- View your plan statistics

## 📁 Project Structure

```
meal-exercise-planner/
├── app.py                 # Main application router and navigation
├── auth.py                # Authentication and user management
├── gemini.py              # Gemini AI integration for plan generation
├── pages_landing.py       # Landing page with features showcase
├── pages_planner.py       # Main planner interface
├── pages_history.py       # Plan history viewer
├── pages_profile.py       # User profile and settings
├── .streamlit/
│   └── config.toml        # Streamlit server configuration
├── main.py                # Replit boilerplate (not used by app)
├── users.json             # User data storage (created automatically)
├── .gitignore             # Git ignore rules
├── README.md              # This file
└── pyproject.toml         # Python dependencies
```

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Google Gemini AI](https://ai.google.dev/)** - AI model for plan generation
- **[Python 3.11](https://www.python.org/)** - Programming language
- **Session State** - User authentication and state management
- **JSON File Storage** - Simple data persistence

## 🔒 Security Note

**Important:** This application uses a simple file-based authentication system for demonstration purposes. 

- Passwords are stored in plain text in `users.json`
- Suitable for personal use and learning
- **NOT recommended for production deployment**

For production use, consider:
- Implementing password hashing (bcrypt, argon2)
- Using a proper database (PostgreSQL, MongoDB)
- Adding email verification
- Using authentication services (Firebase, Supabase, Auth0)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is free to use for personal and educational purposes.

## 💡 Tips for Best Results

1. **Be Specific:** List actual ingredients you have, not just categories
2. **Include Quantities:** Mention if you have limited amounts of certain items
3. **Set Realistic Goals:** Choose goals that match your current fitness level
4. **Save Preferences:** Use the profile page to save default ingredients/equipment
5. **Review History:** Check past plans for ideas and track your progress

## 🐛 Troubleshooting

**App won't start:**
- Ensure Python 3.11+ is installed: `python --version`
- Check that all dependencies are installed: `pip list`
- Verify your GEMINI_API_KEY is set correctly

**Plans not generating:**
- Check your internet connection
- Verify your API key is valid
- Ensure you've filled in all required fields

**Can't sign in:**
- Check if `users.json` exists in the project directory
- Try creating a new account
- Ensure you're using the correct credentials

## 📧 Contact & Support

If you have questions or need help:
- Open an issue on GitHub
- Check the [Gemini AI Documentation](https://ai.google.dev/docs)
- Review [Streamlit Documentation](https://docs.streamlit.io/)

---

**Built with ❤️ using Streamlit and Gemini AI**

*Start your fitness journey today with AI-powered personalized planning!*
