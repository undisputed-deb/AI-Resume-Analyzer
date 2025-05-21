import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ ERROR: Gemini API Key is missing. Check your .env file!")

genai.configure(api_key=GEMINI_API_KEY)

def analyze_resume_with_gemini(resume_text, job_role):
    prompt = f"""
    You are a professional AI resume reviewer. A user uploaded their resume applying for the role of {job_role}.

    Resume Text:
    {resume_text}

    Please analyze and respond in EXACT JSON format:
    {{
      "readability_score": <score from 0 to 100>,
      "grade": "<letter grade A-F>",
      "percentile_rank": <0-100>,
      "resume_verdict": "<a concise verdict>",
      "resume_analysis": ["...", "..."],
      "resume_feedback": ["...", "..."],
      "resume_enhancement": ["...", "..."],
      "resume_strengths": ["...", "..."],
      "resume_weaknesses": ["...", "..."],
      "keyword_match": ["...", "..."]
    }}
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(prompt)
        raw = response.text.strip()

        if raw.startswith("```"):
            raw = raw.strip("`").strip("json").strip()

        return json.loads(raw)

    except Exception as e:
        print("❌ Gemini Error:", e)
        return None
