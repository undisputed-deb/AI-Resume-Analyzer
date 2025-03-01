import google.generativeai as genai
import os
import random
from dotenv import load_dotenv

# Load API Key from .env
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

# Get the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ ERROR: Gemini API Key is missing. Check your .env file!")

# Configure Google Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

def analyze_resume_with_gemini(resume_text, job_role):
    """Send resume text to Gemini AI for expert analysis and return structured data."""
    prompt = f"""
    You are a professional career advisor evaluating resumes for a {job_role} position.

    The candidate's resume text:
    {resume_text}

    Provide the following in a structured format:
    - Readability score (between 1 to 100)
    - Letter grade (A, B, C, D, or F) based on the resume quality
    - Percentile rank (simulated as a percentage)
    - Expert verdict: A brief analysis of the resume for a {job_role} role
    - Additional recommendations to improve the resume
    
    Return the response in JSON format like this:
    {{
      "readability_score": <score>,
      "grade": "<letter>",
      "percentile_rank": <percentage>,
      "expert_verdict": "<analysis>",
      "improvement_suggestions": ["suggestion1", "suggestion2"]
    }}
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text  # Return the JSON response from Gemini
