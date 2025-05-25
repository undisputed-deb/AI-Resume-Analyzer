# 📊 AI Resume Analyzer

🚀 An AI-powered web application that intelligently evaluates resumes for strengths, weaknesses, ATS optimization, keyword matching, and readability using **Google Gemini Pro** and NLP techniques.

👉 **GitHub Repository:** [https://github.com/undisputed-deb/AI-Resume-Analyzer](https://github.com/undisputed-deb/AI-Resume-Analyzer)

---

## 📌 Key Features

✅ **Dynamic Resume Evaluation** – Each resume gets custom feedback, verdict, and improvement tips  
🔍 **Keyword Match Insights** – Detects missing and matched job-relevant keywords  
📊 **Scoring Metrics** – Skills & Experience, Leadership, Certifications & ATS Optimization  
🧠 **Gemini AI Integration** – Uses Gemini Pro to generate expert verdicts and resume breakdowns  
🎨 **Animated & Interactive UI** – Real-time scanning animation, color-coded scores, and modern design  
📋 **Strengths & Weaknesses** – Instantly see what's working and what needs fixing  
🚧 **Enhancement Suggestions** – Actionable improvements for better job application outcomes  

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS, Bootstrap, jQuery  
- **AI Integration:** Google Gemini Pro (via `google.generativeai`)  
- **PDF & DOCX Parsing:** PyMuPDF (`fitz`), `python-docx`

---

## 📁 Project Structure


 📂 AI-Resume-Analyzer
├── app.py # Main Flask backend
├── .env # Stores Gemini API key
├── requirements.txt # All Python dependencies
│
├── templates/
│ ├── index.html # Upload interface
│ └── result.html # Result analysis page
│
├── static/ # Custom CSS & JS
│
├── modules/
│ ├── extract.py # Extract text from PDF/DOCX
│ ├── preprocess.py # Clean and preprocess text
│ ├── gemini_integration.py # Gemini AI integration logic
│
├── uploads/ # Folder for uploaded resumes
└── README.md # This file

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/undisputed-deb/AI-Resume-Analyzer.git
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
GEMINI_API_KEY=your_gemini_api_key_here
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
| Metric                      | Description                                   |
| --------------------------- | --------------------------------------------- |
| 🛠 Skills & Experience      | Technical and domain-related strengths        |
| 🎯 Leadership & Soft Skills | Collaboration, communication, and leadership  |
| 📜 Certifications & ATS     | Industry credentials and ATS-ready format     |
| 🔍 Keyword Match            | Job-specific keyword matching results         |
| 🚧 Weaknesses               | Structural/content gaps and formatting issues |
| 🌟 Strengths                | Highlighted resume positives                  |
| 📝 Feedback & Suggestions   | Gemini-generated actionable recommendations   |

📸 UI Highlights
🌀 Scanning Animation Loader

📈 Colored Score Circles

📦 Sectioned Feedback Boxes

🎨 Smooth UI with hover & entry animations

⚡ One-click resume insights


🧠 Future Enhancements
🧾 PDF download of results

🤖 AI resume rewriting

📬 Email result summary

🧠 Auto comparison with pasted job descriptions

Fork the repository.
Create a feature branch (git checkout -b feature-xyz).
Commit changes (git commit -m "Added feature xyz").
Push to your branch (git push origin feature-xyz).
Create a Pull Request.
📜 License
MIT License © 2025 Debashrestha Nandi
Fork it, build on it, and contribute to better job-hunting tech!
