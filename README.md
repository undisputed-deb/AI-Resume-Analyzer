# 📊 AI Resume Analyzer

**Intelligent resume evaluation powered by Google Gemini Pro AI for ATS optimization, keyword matching, and comprehensive feedback.**

[![Tech Stack](https://img.shields.io/badge/Stack-Python%20%7C%20Flask%20%7C%20Gemini%20AI-blue)](/)
[![License](https://img.shields.io/badge/License-MIT-green)](/)
[![Status](https://img.shields.io/badge/Status-Active-success)](/)
[![AI Powered](https://img.shields.io/badge/AI-Gemini%20Pro-orange)](/)

> **Transform your job search with AI insights.** Upload your resume and get instant analysis with strengths, weaknesses, ATS optimization tips, and keyword matching for any job role.

**🔗 Live Demo:** [AI Resume Analyzer](https://github.com/undisputed-deb/AI-Resume-Analyzer)

---

## ✨ Features

### 🎯 **Smart Resume Analysis**
- **Dynamic Evaluation**: Custom feedback for each resume
- **ATS Optimization**: Ensure your resume passes Applicant Tracking Systems
- **Keyword Intelligence**: Detect missing and matched job-relevant keywords
- **Multi-format Support**: Process PDF and DOCX files seamlessly

### 🧠 **AI-Powered Insights**
- **Gemini Pro Integration**: Expert-level resume analysis
- **Comprehensive Scoring**: Skills, Experience, Leadership, and Certifications
- **Verdict Generation**: AI-driven recommendations and improvements
- **Real-time Processing**: Instant analysis with animated feedback

### 📊 **Detailed Metrics**
- **Skills & Experience Scoring** (0-100%)
- **Leadership & Soft Skills Analysis**
- **Certification & ATS Readiness**
- **Keyword Match Percentage**
- **Strengths & Weaknesses Breakdown**

### 🎨 **Modern Interface**
- **Animated UI**: Real-time scanning animations
- **Color-coded Scores**: Visual feedback system
- **Responsive Design**: Works on all devices
- **Interactive Elements**: Smooth hover effects and transitions

---

## 🏗️ Architecture

```
AI-Resume-Analyzer/
├── app.py                    # Flask application entry point
├── .env                      # Environment variables (API keys)
├── requirements.txt          # Python dependencies
│
├── templates/               # HTML templates
│   ├── index.html          # Resume upload interface
│   └── result.html         # Analysis results page
│
├── static/                 # Static assets
│   ├── css/               # Custom stylesheets
│   ├── js/                # JavaScript files
│   └── images/            # UI assets
│
├── modules/               # Core functionality
│   ├── extract.py        # PDF/DOCX text extraction
│   ├── preprocess.py     # Text cleaning & preprocessing
│   └── gemini_integration.py # AI analysis logic
│
├── uploads/              # Temporary file storage
└── README.md            # Project documentation
```

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+**
- **Google AI API Key** (Gemini Pro)
- **pip** package manager

### 1. Clone & Setup

```bash
git clone https://github.com/undisputed-deb/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Environment Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Keys

```bash
# Create .env file
touch .env

# Add your Gemini API key
echo "GEMINI_API_KEY=your_gemini_api_key_here" >> .env
```

**Get your Gemini API key:**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy and paste into your `.env` file

### 4. Run the Application

```bash
python app.py
```

**🌐 Open your browser and navigate to:**
```
http://127.0.0.1:5000
```

---

## 🎯 Usage Guide

### Step-by-Step Analysis

1. **📄 Upload Resume**
   - Drag & drop or select your resume file
   - Supports PDF and DOCX formats
   - Maximum file size: 10MB

2. **🎯 Specify Job Role**
   - Enter the target position you're applying for
   - Be specific (e.g., "Senior Software Engineer", "Data Scientist")

3. **🔍 Analyze**
   - Click "Analyze Resume" button
   - Watch real-time scanning animation
   - Processing typically takes 10-30 seconds

4. **📊 Review Results**
   - View comprehensive scoring metrics
   - Read AI-generated feedback and suggestions
   - Download or save analysis for future reference

### Analysis Metrics

| Metric | Description | Range |
|--------|-------------|-------|
| 🛠️ **Skills & Experience** | Technical competencies and domain expertise | 0-100% |
| 🎯 **Leadership & Soft Skills** | Communication, teamwork, and leadership qualities | 0-100% |
| 📜 **Certifications & ATS** | Industry credentials and ATS optimization | 0-100% |
| 🔍 **Keyword Match** | Job-specific keyword alignment | 0-100% |
| 🌟 **Strengths** | Resume highlights and competitive advantages | Qualitative |
| 🚧 **Weaknesses** | Areas needing improvement | Qualitative |
| 💡 **Suggestions** | Actionable enhancement recommendations | Qualitative |

---

## 🛠️ Tech Stack

### Backend
- **Python 3.8+** - Core programming language
- **Flask** - Lightweight web framework
- **Google Gemini Pro** - Advanced AI analysis
- **PyMuPDF (fitz)** - PDF text extraction
- **python-docx** - DOCX file processing

### Frontend
- **HTML5** - Modern markup
- **CSS3** - Advanced styling with animations
- **Bootstrap 5** - Responsive framework
- **jQuery** - Dynamic interactions
- **Font Awesome** - Icon library

### AI & NLP
- **Google AI SDK** - Gemini Pro integration
- **NLTK** - Natural language processing
- **Regular Expressions** - Text pattern matching

---

## 📊 API Reference

### Upload & Analyze Resume

```http
POST /analyze
Content-Type: multipart/form-data

{
  "resume": <file>,
  "job_role": "Software Engineer"
}
```

**Response:**
```json
{
  "scores": {
    "skills_experience": 85,
    "leadership": 78,
    "certifications_ats": 92,
    "keyword_match": 67
  },
  "analysis": {
    "strengths": ["Strong technical background", "Relevant experience"],
    "weaknesses": ["Missing soft skills", "No leadership examples"],
    "suggestions": ["Add project management experience", "Include team collaboration examples"],
    "verdict": "Strong candidate with room for improvement in soft skills demonstration"
  },
  "keywords": {
    "matched": ["Python", "Machine Learning", "API"],
    "missing": ["Docker", "Kubernetes", "Agile"]
  }
}
```

---

## 🎨 UI Highlights

### Visual Features
- **🌀 Loading Animations** - Engaging scanning effects during analysis
- **📈 Progress Circles** - Color-coded scoring visualization
- **📦 Card Layout** - Organized information sections
- **🎯 Hover Effects** - Interactive element feedback
- **📱 Responsive Design** - Mobile-friendly interface

### Color Scheme
- **🟢 Excellent (80-100%)** - Green indicators
- **🟡 Good (60-79%)** - Yellow indicators  
- **🟠 Fair (40-59%)** - Orange indicators
- **🔴 Poor (0-39%)** - Red indicators

---

## 🔧 Configuration

### Environment Variables

```bash
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional
FLASK_ENV=development
FLASK_DEBUG=True
MAX_FILE_SIZE=10485760  # 10MB in bytes
ALLOWED_EXTENSIONS=pdf,docx
```

### File Upload Limits

```python
# app.py configuration
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {'pdf', 'docx'}
```

---

## 🚀 Deployment

### Local Development
Follow the Quick Start guide above.

### Production Deployment

**Recommended Platforms:**
- **Heroku** - Easy Python deployment
- **Railway** - Modern hosting platform
- **Vercel** - Serverless functions
- **DigitalOcean App Platform** - Managed hosting

**Example Heroku Deployment:**

```bash
# Create Procfile
echo "web: python app.py" > Procfile

# Deploy to Heroku
heroku create your-app-name
git push heroku main
heroku config:set GEMINI_API_KEY=your_api_key_here
```

---

## 🧪 Testing

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-flask

# Run tests
pytest tests/

# Run with coverage
pytest --cov=app tests/
```

### Manual Testing Checklist

- [ ] PDF resume upload and analysis
- [ ] DOCX resume upload and analysis
- [ ] Various job role inputs
- [ ] Error handling for invalid files
- [ ] Response time under 30 seconds
- [ ] Mobile responsiveness
- [ ] Score accuracy validation

---

## 🌟 Future Enhancements

### Planned Features
- **📄 PDF Report Export** - Download detailed analysis reports
- **🤖 AI Resume Rewriting** - Auto-improve resume content
- **📧 Email Integration** - Send results via email
- **🔄 Batch Processing** - Analyze multiple resumes
- **📊 Analytics Dashboard** - Track improvement over time
- **🎯 Job Description Comparison** - Direct JD matching
- **🌐 Multi-language Support** - International resume analysis

### Technical Improvements
- **Redis Caching** - Faster repeat analyses
- **Database Integration** - User history and analytics
- **API Rate Limiting** - Enhanced security
- **Containerization** - Docker deployment
- **CI/CD Pipeline** - Automated testing and deployment

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup

1. **Fork the repository**
2. **Create feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Add tests** for new functionality
5. **Commit changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
6. **Push to branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Create Pull Request**

### Contribution Guidelines

- Follow PEP 8 Python style guidelines
- Add docstrings to all functions
- Include tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Debashrestha Nandi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **Google AI Team** for Gemini Pro API
- **Flask Community** for the excellent web framework
- **Bootstrap Team** for responsive design components
- **Open Source Contributors** who inspire continuous improvement

---

## 📞 Contact & Support

**Debashrestha Nandi**
- 📧 **Email:** [deb86011@gmail.com](mailto:deb86011@gmail.com)
- 💼 **LinkedIn:** [Debashrestha Nandi](https://www.linkedin.com/in/debashrestha-nandi-a7343b171/)
- 🐙 **GitHub:** [@undisputed-deb](https://github.com/undisputed-deb)
- 🌐 **Portfolio:** [Your Portfolio URL]

### Support

- **🐛 Bug Reports:** [GitHub Issues](https://github.com/undisputed-deb/AI-Resume-Analyzer/issues)
- **💡 Feature Requests:** [GitHub Discussions](https://github.com/undisputed-deb/AI-Resume-Analyzer/discussions)
- **📖 Documentation:** [Project Wiki](https://github.com/undisputed-deb/AI-Resume-Analyzer/wiki)

---

<div align="center">

**⭐ Star this repository if it helped improve your resume! ⭐**

*Empowering job seekers with AI-driven resume intelligence.*

[![GitHub stars](https://img.shields.io/github/stars/undisputed-deb/AI-Resume-Analyzer?style=social)](https://github.com/undisputed-deb/AI-Resume-Analyzer/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/undisputed-deb/AI-Resume-Analyzer?style=social)](https://github.com/undisputed-deb/AI-Resume-Analyzer/network/members)

</div>
