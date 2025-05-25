import os
import time
from flask import Flask, request, render_template
from modules.extract import extract_text_from_pdf, extract_text_from_docx
from modules.preprocess import preprocess_text
from modules.gemini_integration import analyze_resume_with_gemini  # Gemini integration

print(" Flask app starting...")

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def upload_resume():
    if request.method == "POST":
        job_role = request.form.get("job_role", "").strip()
        if "resume" not in request.files or not job_role:
            return render_template("index.html", error="❌ Please enter a job role and upload a valid file!")

        file = request.files["resume"]
        if file.filename == "":
            return render_template("index.html", error="❌ No selected file!")

        filename = os.path.basename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        # Extract and clean resume text
        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif filename.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            return render_template("index.html", error="❌ Unsupported file format!")

        cleaned_text = preprocess_text(text)

        # Simulate delay
        time.sleep(2)

        # Call Gemini API
        feedback = analyze_resume_with_gemini(cleaned_text, job_role)

        if not feedback:
            return render_template("index.html", error="⚠️ Unable to analyze resume. Please try again.")

        # Construct analysis dictionary for result.html
        analysis = {
            "job_role": job_role,
            "overall_score": round((feedback.get("readability_score", 70) + feedback.get("percentile_rank", 60)) / 2),
            "readability_score": feedback.get("readability_score", 70),
            "percentile_rank": feedback.get("percentile_rank", 60),
            "grade": feedback.get("grade", "B"),
            "resume_verdict": feedback.get("resume_verdict", "⚠️ No verdict returned."),
            "resume_analysis": feedback.get("resume_analysis", []),
            "resume_feedback": feedback.get("resume_feedback", []),
            "resume_enhancement": feedback.get("resume_enhancement", []),
            "resume_strengths": feedback.get("resume_strengths", []),
            "resume_weaknesses": feedback.get("resume_weaknesses", []),
            "keyword_match": feedback.get("keyword_match", [])
        }

        return render_template("result.html", analysis=analysis)

    return render_template("index.html")

if __name__ == "__main__":
    print("✅ Running Flask on http://127.0.0.1:5000")
    app.run(debug=True)
