📊 AI Resume Analyzer

🚀 An AI-powered resume analysis tool that evaluates resumes for strengths, weaknesses, ATS optimization, and keyword matching to improve job application success — now enhanced with Gemini AI integration.

---
📌 Features

- ✅ Dynamic Resume Analysis – Personalized strengths, weaknesses, and expert feedback powered by Gemini AI.
- 🔍 Keyword Match Insights – Identifies missing and matched keywords relevant to the job role.
- 📊 Scoring System – Rates:
  - Skills & Experience
  - Leadership & Soft Skills
  - Certifications & ATS Optimization
- 🚀 Resume Enhancement Suggestions – Actionable improvement tips.
- 🎯 Real-Time ATS Compatibility Check – Simulates how recruiters and ATS systems evaluate your resume.
- 🤖 Gemini AI Integration – Uses gemini-pro or gemini-1.5-pro to generate resume verdicts, scores, suggestions, and keyword insights.
- 🎨 Interactive UI – Animated scan effects and colorful result boxes for a modern experience.

---

## 🛠️ Tech Stack

| Layer      | Technologies                                    |
|------------|-------------------------------------------------|
| Backend    | Flask (Python)                                  |
| Frontend   | HTML, CSS   |
| AI         | Google Gemini API (`gemini-pro`, `gemini-1.5-pro`) |
| Parsing    | PyMuPDF (`fitz`),
Resume Processing Modules:
extract_text_from_pdf()
extract_text_from_docx()
preprocess_text()
evaluate_resume()
📂 Project Structure
php
Copy
Edit
📂 AI-Resume-Analyzer
│── app.py                  # Main Flask application
│── templates/
│   │── index.html           # Upload page
│   │── result.html          # Resume analysis results page
│── static/
│   │── styles.css           # Custom styles
│   │── script.js            # jQuery animations
│── modules/
│   │── extract.py           # PDF & Docx extraction logic
│   │── preprocess.py        # Text cleaning & preprocessing
│   │── analyze.py           # Resume evaluation logic
│── uploads/                 # Stores uploaded resumes
│── README.md                # Project documentation
│── requirements.txt         # Python dependencies
│── .gitignore               # Ignore unnecessary files
📥 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
2️⃣ Create a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy
Edit
python app.py
✅ Open http://127.0.0.1:5000/ in your browser to start analyzing resumes!

📜 Usage Guide
Upload your resume (PDF or DOCX format).
Enter the job role you are applying for.
Click Analyze Resume.
View scores, keyword insights, strengths, weaknesses, feedback, and suggestions.
Improve your resume based on the recommendations.
📊 Score Breakdown
Metric	Description
🛠 Skills & Experience	Evaluates technical and job-related skills.
🎯 Leadership & Soft Skills	Assesses leadership, teamwork, and communication skills.
📜 Certifications & ATS Optimization	Checks if certifications and keywords align with industry standards.
🔍 Keyword Match Insights	Detects missing and relevant job-related keywords.
🚧 Areas for Improvement	Highlights formatting, content, and ATS-related issues.
🌟 Resume Strengths	Identifies key highlights and strong points of your resume.
🚀 Overall Verdict	Provides a final assessment and resume quality rating.
📸 Screenshots
🔍 Scanning Effect

📊 Resume Score Breakdown

🚀 Enhancement Suggestions

🛠 Future Enhancements
🧠 AI-Powered Resume Recommendations – Generate AI-based resume improvements.
📄 Resume PDF Export – Download analyzed results in PDF format.
🔍 Job Description Matching – Automatically compare resume with job descriptions.
📬 Email Alerts – Send improvement reports via email.
💡 Contributing
🚀 Contributions are welcome! If you'd like to improve this project:

Fork the repository.
Create a feature branch (git checkout -b feature-xyz).
Commit changes (git commit -m "Added feature xyz").
Push to your branch (git push origin feature-xyz).
Create a Pull Request.
📄 License
MIT License © 2024 Your Name
