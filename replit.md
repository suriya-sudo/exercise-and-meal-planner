# Replit Agent Guide

## Overview

AI-Powered Meal & Exercise Planner is a personalized fitness planning application built with Streamlit and Google's Gemini AI. The application generates customized weekly meal plans and exercise routines based on user-specific fitness goals, available ingredients, and home equipment. Users can authenticate, save their plans, and track their fitness journey over time.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Framework: Streamlit**
- Single-page application with multi-page navigation using session state
- Page-based routing system without Streamlit's built-in multipage feature
- Pages are modularized into separate files: `pages_landing.py`, `pages_planner.py`, `pages_history.py`, `pages_profile.py`
- Navigation managed through sidebar with conditional rendering based on authentication state
- Custom CSS styling for hero sections and feature cards on landing page

**Rationale:** Streamlit was chosen for rapid prototyping and deployment, with custom page routing providing more control over navigation flow and authentication state management.

### Backend Architecture

**Authentication System**
- File-based authentication using JSON storage (`users.json`)
- Session state management for user authentication and navigation
- User data includes: username, password (plaintext), email, creation date, fitness preferences, and plan history
- No encryption or password hashing implemented

**Rationale:** Simple JSON-based storage provides quick implementation for MVP without database overhead. This approach has limitations for production use regarding security and scalability.

**State Management**
- Centralized session state initialization in `auth.py`
- Session state tracks: authentication status, username, user data, current page, and plan history
- State persisted across page navigation using Streamlit's built-in session management

**AI Integration**
- Google Gemini AI (genai SDK) for content generation
- Uses `gemini-2.5-pro` model as specified in code comments
- Two primary AI functions: `generate_meal_plan()` and `generate_exercise_plan()`
- Prompt engineering with structured output requirements (daily breakdowns with calories, macros, exercise details)

**Rationale:** Gemini AI provides powerful natural language generation capabilities for creating personalized, contextual fitness content. The structured prompts ensure consistent output formatting for user readability.

### Data Storage Solutions

**User Data Storage**
- Format: JSON file (`users.json`)
- Structure: Dictionary with username as key, containing user profile and plan history
- No database backend; all data stored in single file
- Plan history embedded within user objects as arrays

**Limitations:**
- No concurrent write protection
- Data loss risk without backup mechanisms
- Scalability concerns with growing user base
- No data relationships or complex querying capabilities

**Alternatives Considered:** SQLite or PostgreSQL could provide better data integrity, concurrent access handling, and scalability, but add deployment complexity.

### Authentication and Authorization

**Current Implementation:**
- Basic username/password authentication
- Passwords stored in plaintext in JSON file
- No token-based authentication or session expiration
- Authorization based solely on session state

**Security Concerns:**
- No password hashing (bcrypt, argon2 not implemented)
- No HTTPS enforcement mentioned
- No rate limiting on authentication attempts
- Session state could be vulnerable to manipulation

**Recommended Improvements:** Implement password hashing, add session tokens, implement proper logout functionality, and consider OAuth integration for production use.

### Application Flow

1. **Landing Page** → Authentication (Sign Up/Sign In)
2. **Authenticated State** → Navigation sidebar appears with three main pages:
   - Planner (Home): Generate new meal/exercise plans
   - History: View and manage saved plans
   - Profile: Edit preferences and account settings
3. **Plan Generation Flow:**
   - User inputs goals, ingredients, equipment
   - AI generates personalized content
   - Plan automatically saved to user history
   - User can view in history page

## External Dependencies

### Third-Party APIs

**Google Gemini AI API**
- Purpose: Generate personalized meal plans and exercise routines
- SDK: `google-genai` (formerly `google-generativeai`)
- Model: `gemini-2.5-pro`
- Authentication: API key via environment variable `GEMINI_API_KEY`
- Rate Limits: Subject to Google's API quotas (not handled in code)
- Error Handling: Basic exception handling; API key validation on client creation

### Python Libraries

**Core Framework:**
- `streamlit`: Web application framework for UI and routing

**AI/ML:**
- `google-genai`: Google's Gemini AI SDK for content generation

**Standard Library:**
- `json`: User data persistence
- `os`: Environment variable access
- `datetime`: Timestamp generation for plans and user creation

### Environment Configuration

**Required Environment Variables:**
- `GEMINI_API_KEY`: Google Gemini API key (mandatory for AI functionality)

**Deployment Considerations:**
- Designed for Replit deployment with Secrets management
- Can run locally with environment variables set
- No database connection strings required
- No additional service credentials needed

### External Services

**Current Integrations:** None beyond Gemini AI

**Potential Future Integrations:**
- Email service for user verification and notifications
- Cloud storage for user data backup
- Analytics service for usage tracking
- Payment gateway if premium features added
- Nutrition database API for enhanced meal information