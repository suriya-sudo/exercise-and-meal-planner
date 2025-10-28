import streamlit as st

def show_landing_page():
    """Display the modern landing page."""
    
    st.markdown("""
        <style>
        .hero-section {
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
            color: white;
            margin-bottom: 2rem;
        }
        .hero-title {
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .hero-subtitle {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        .feature-card {
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            margin: 1rem 0;
            border: 1px solid #e9ecef;
        }
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        .feature-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: #333;
        }
        .feature-description {
            color: #666;
            font-size: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">🏋️ Meal & Exercise Planner</div>
            <div class="hero-subtitle">AI-Powered Personalized Fitness Plans</div>
            <p>Transform your fitness journey with customized meal and workout plans tailored to your goals, ingredients, and equipment.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🚀 Get Started", type="primary", use_container_width=True):
            st.session_state.current_page = 'auth'
            st.rerun()
    
    with col2:
        if st.button("📝 Sign In", use_container_width=True):
            st.session_state.current_page = 'auth'
            st.rerun()
    
    st.markdown("---")
    st.markdown("## ✨ Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🍽️</div>
                <div class="feature-title">Smart Meal Plans</div>
                <div class="feature-description">Get weekly meal plans based on your pantry ingredients and fitness goals</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">💪</div>
                <div class="feature-title">Custom Workouts</div>
                <div class="feature-description">Personalized exercise routines designed for your equipment and fitness level</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <div class="feature-title">Track Progress</div>
                <div class="feature-description">View your plan history and monitor your fitness journey</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## 🎯 How It Works")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 1️⃣ Set Your Goal")
        st.write("Choose between weight loss, weight gain, or maintenance")
    
    with col2:
        st.markdown("### 2️⃣ Enter Your Resources")
        st.write("List your pantry ingredients and exercise equipment")
    
    with col3:
        st.markdown("### 3️⃣ Get Your Plan")
        st.write("Receive AI-generated weekly meal and exercise plans")
    
    st.markdown("---")
    
    st.markdown("""
        <div style='text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 10px;'>
            <h2>Ready to Start Your Fitness Journey?</h2>
            <p style='font-size: 1.2rem; color: #666; margin-bottom: 1.5rem;'>Join thousands of users transforming their health with AI-powered planning</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎉 Create Free Account", type="primary", use_container_width=True):
            st.session_state.current_page = 'auth'
            st.rerun()
