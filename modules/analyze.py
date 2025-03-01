import re
import textstat

# Predefined job-specific keyword expectations
JOB_KEYWORDS = {
    "Software Engineer": ["Python", "Java", "Software Development", "Agile", "Algorithms", "Data Structures"],
    "Cybersecurity Specialist": ["Network Security", "Encryption", "Risk Assessment", "Penetration Testing", "Compliance"],
    "Civil Engineer": ["Structural Design", "AutoCAD", "Construction Management", "Surveying", "Geotechnical Engineering"],
    "Data Scientist": ["Machine Learning", "Statistics", "Python", "Data Analysis", "Big Data"],
    "Marketing Manager": ["SEO", "Social Media", "Campaign Strategy", "Branding", "Content Marketing"]
}

# Predefined industry-specific verdicts
JOB_VERDICTS = {
    "Software Engineer": "A strong resume should highlight programming skills, experience with frameworks, and problem-solving abilities.",
    "Cybersecurity Specialist": "Emphasizing security certifications and risk mitigation strategies will enhance this resume.",
    "Civil Engineer": "Showcasing experience with infrastructure projects, CAD tools, and compliance knowledge is crucial.",
    "Data Scientist": "Highlighting statistical skills, machine learning projects, and data processing techniques will add value.",
    "Marketing Manager": "A good resume for marketing should emphasize campaign success metrics, digital strategies, and branding expertise."
}

def clean_text(text):
    """Remove special characters and extra spaces."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9.,!? ]', '', text)
    return text.strip()

def evaluate_resume(text, job_role):
    """Analyze readability, missing keywords, and job suitability."""
    text = clean_text(text)

    readability = textstat.flesch_reading_ease(text)
    if readability < 0:
        readability = 0  # Set minimum readability

    # Determine missing job-specific keywords
    required_keywords = JOB_KEYWORDS.get(job_role, [])
    missing_keywords = [kw for kw in required_keywords if kw.lower() not in text.lower()]

    # Get industry verdict
    verdict = JOB_VERDICTS.get(job_role, "No verdict available for this job category.")

    return {
        "readability_score": round(readability, 2),
        "missing_keywords": missing_keywords,
        "verdict": verdict
    }
