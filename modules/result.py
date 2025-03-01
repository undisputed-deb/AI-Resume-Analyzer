from flask import Flask, request, render_template
import os
from modules.extract import extract_text_from_pdf, extract_text_from_docx
from modules.preprocess import preprocess_text
from modules.analyze import evaluate_resume
import time  # Simulating scanning effect

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

        text = ""
        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif filename.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            return render_template("index.html", error="❌ Unsupported file format!")

        cleaned_text = preprocess_text(text)

        # Simulating scanning animation effect
        time.sleep(2)  # Adds delay for better user experience

        # Evaluate resume with AI
        feedback = evaluate_resume(cleaned_text, job_role)

        # Ensure `analysis` is always defined to prevent errors
        analysis = {
            "job_role": job_role,
            "resume_score": feedback.get("match_score", 0),
            "readability_score": feedback.get("readability_score", "N/A"),
            "requirements_score": feedback.get("requirements_score", 0),
            "keywords_score": feedback.get("keywords_score", 0),
            "requirements_analysis": feedback.get("requirements_analysis", []),
            "resume_feedback": feedback.get("feedback", []),
            "suggestions": [
                "✔ Add measurable achievements.",
                "✔ Use action verbs for impact.",
                "✔ Improve formatting for readability.",
                "✔ Include relevant technical skills."
            ]
        }

        return render_template("result.html", analysis=analysis)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
