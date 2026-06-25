# InternReady AI

InternReady AI is a Streamlit-based career roadmap tool for students preparing for internships, projects, and skill development. It combines rule-based logic with AI (powered by Google Gemini) to give personalized, conversational guidance.

## Features

- Personalized roadmap generation (rule-based)
- AI-generated personalized roadmap (powered by Gemini)
- Domain-specific skills and project ideas
- Learning resources
- Internship readiness score
- Personalized advice
- Downloadable roadmap
- Progress checklist
- AI Mentor Chat — conversational chatbot with memory for internship and career doubts
- AI-powered Resume Helper — generates professional resume bullet points
- AI-powered LinkedIn Helper — generates LinkedIn project announcement captions
- GitHub presentation tips

## Tech Stack

- Python
- Streamlit
- Google Gemini API (google-genai)
- Rule-based recommendation logic

## Project Structure

```text
internready-ai/
  Home.py
  pages/
    1_Roadmap_Generator.py
    2_Student_Toolkit.py
    3_AI_Mentor_Chat.py
  requirements.txt
  README.md
  .streamlit/
    secrets.toml
```

## Setup

1. Clone this repository
2. Install dependencies:
3. Add your Gemini API key in `.streamlit/secrets.toml`:
```toml
   GEMINI_API_KEY = "your_api_key_here"
```
4. Run the app:
```
streamlit run Home.py
```