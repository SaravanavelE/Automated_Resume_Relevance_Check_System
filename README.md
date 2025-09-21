# Automated_Resume_Relevance_Check_System
AI-powered resume evaluation engine that combines rule-based checks with LLM-based semantic understanding.

---

## ✨ Features
- Upload resume (PDF/DOCX)
- Upload job description (PDF/DOCX)
- System checks:
  - Required skills (must have)
  - Optional skills (good to have)
  - Semantic similarity (meaning-based match)
- Gives a **score out of 100**
- Verdict shown as **High / Medium / Low** with colored output
- Dark theme UI for better readability

---

## 🛠️ Tech Used
- Python 3.11
- Flask (backend + HTML rendering)
- PyMuPDF & python-docx (to extract text)
- Sentence Transformers (for embeddings)
- Basic HTML + CSS (dark theme design)

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>

Create a virtual environment (optional but recommended):
python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate  # on Mac/Linux


Install dependencies:
pip install -r requirements.txt

▶️ Run the App
python app.py

Open your browser at http://127.0.0.1:5000/

📂 Project Structure
project/
│── app.py               # Flask application
│── requirements.txt     # Dependencies
│── templates/           # HTML files
│   ├── index.html
│   └── results.html
│── static/              # CSS and static assets
│   └── style.css
│── uploads/             # Uploaded resumes/JDs (ignored in git)
│── README.md

🚀 Example
Upload your resume and a job description.
The system scores them and highlights missing skills.

Verdict is shown in colors:
🟢 High (75–100)
🟠 Medium (50–74)
🔴 Low (<50)

🙌 Notes
Keywords (must_have and good_to_have) are currently hardcoded for demo.
In a real project, they can be extracted automatically from the JD.
Uploaded files are stored temporarily inside the uploads/ folder.
