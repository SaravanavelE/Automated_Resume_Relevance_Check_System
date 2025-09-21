# Automated_Resume_Relevance_Check_System
AI-powered resume evaluation engine that combines rule-based checks with LLM-based semantic understanding.
---

## 🎥 Project Demo Video
Watch the demo on [click_here](https://drive.google.com/file/d/YOUR_FILE_ID/view?usp=sharing](https://drive.google.com/file/d/1LwXcP8V37r61GzAnYQ5xXt7dk1K-wXtS/view?usp=sharing)

---

## Objective
The Automated Resume Relevance Check System will:
- Automate resume evaluation against job requirements at scale.
- Generate a Relevance Score (0–100) for each resume per job role.
- Highlight gaps such as missing skills, certifications, or projects.
- Provide a fit verdict (High / Medium / Low suitability) to recruiters.
- Offer personalized improvement feedback to students.
- Store evaluations in a web-based dashboard accessible to the placement team.
This system should be robust, scalable, and flexible enough to handle thousands of resumes weekly.

---

## 🚀 Workflow

### 1. Job Requirement Upload
- Placement team uploads the job description (JD) into the system.  

### 2. Resume Upload
- Students submit resumes (PDF/DOCX) while applying.  

### 3. Resume Parsing
- Extracts raw text from PDF/DOCX.  
- Cleans and standardizes the format by removing headers/footers and normalizing sections.  

### 4. JD Parsing
- Extracts key details such as:
  - Role title  
  - Must-have skills  
  - Good-to-have skills  
  - Required qualifications  

### 5. Relevance Analysis
1. **Hard Match** → Exact and fuzzy keyword/skill checks.  
2. **Semantic Match** → Embedding similarity between resume and JD using LLMs.  
3. **Scoring & Verdict** → Weighted scoring formula to generate final score.  

### 6. Output Generation
- Relevance Score (0–100)  
- Missing skills, certifications, or projects  
- Verdict: **High / Medium / Low suitability**  
- Suggestions for improving the resume  

### 7. Storage & Access
- Results stored in a database.  
- Placement team can search/filter resumes by job role, score, and location.  

### 8. Web Application
- **Placement Dashboard** → Upload JD, see shortlisted resumes with scores.  
- **Student Module** → Upload resume and view feedback.  

---

## 🛠️ Tech Stack

- **Programming**: Python  
- **Document Parsing**: PyMuPDF / pdfplumber, python-docx / docx2txt  
- **NLP & AI**: spaCy, NLTK, HuggingFace Transformers  
- **LLM Workflow**: LangChain, LangGraph, LangSmith  
- **Vector Databases**: Chroma / FAISS / Pinecone (for embeddings & semantic search)  
- **Models**: OpenAI GPT, Gemini, Claude, HuggingFace models  
- **Matching Techniques**: TF-IDF, BM25, fuzzy matching, embeddings + cosine similarity  
- **Scoring**: Weighted combination of hard match + semantic similarity  

---

---

## Features
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
