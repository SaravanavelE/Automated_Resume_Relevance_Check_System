import os
import re
import fitz               # PyMuPDF for PDF text extraction
import docx               # python-docx for Word files
from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer, util

# ---------------- Flask Setup ---------------- #
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Preload sentence transformer model (small + fast)
model = SentenceTransformer("all-MiniLM-L6-v2")


# ---------------- Helper Functions ---------------- #
def extract_text(path):
    """
    Read text from a PDF or DOCX file.
    """
    text = ""
    ext = path.split(".")[-1].lower()

    if ext == "pdf":
        with fitz.open(path) as pdf:
            for page in pdf:
                text += page.get_text()

    elif ext in ["docx", "doc"]:
        document = docx.Document(path)
        for para in document.paragraphs:
            text += para.text + "\n"

    return text


def clean(text):
    """Normalize whitespace and lowercase."""
    return re.sub(r"\s+", " ", text).strip().lower()


def keyword_match(resume_text, keywords):
    """
    Check if keywords appear in resume.
    Returns score and missing keywords.
    """
    found = 0
    missing = []

    for word in keywords:
        if word.lower() in resume_text:
            found += 1
        else:
            missing.append(word)

    return found, missing


def evaluate_resume(resume_text, jd_text, must_have, good_to_have):
    """
    Combine keyword matching and semantic similarity
    to produce a final relevance score.
    """
    resume_clean = clean(resume_text)
    jd_clean = clean(jd_text)

    # --- Keyword-based scoring (hard match) ---
    must_score, must_missing = keyword_match(resume_clean, must_have)
    good_score, good_missing = keyword_match(resume_clean, good_to_have)

    total_possible = len(must_have) * 2 + len(good_to_have)
    hard_score = (must_score * 2 + good_score) / total_possible * 50

    # --- Semantic similarity ---
    emb_resume = model.encode(resume_clean, convert_to_tensor=True)
    emb_jd = model.encode(jd_clean, convert_to_tensor=True)
    semantic_score = util.pytorch_cos_sim(emb_resume, emb_jd).item() * 50

    # --- Final aggregation ---
    final_score = round(hard_score + semantic_score, 2)

    if final_score >= 75:
        verdict = "High"
    elif final_score >= 50:
        verdict = "Medium"
    else:
        verdict = "Low"

    return final_score, verdict, must_missing + good_missing


# ---------------- Routes ---------------- #
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Save uploaded files
        resume_file = request.files["resume"]
        jd_file = request.files["jd"]

        resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_file.filename)
        jd_path = os.path.join(app.config["UPLOAD_FOLDER"], jd_file.filename)

        resume_file.save(resume_path)
        jd_file.save(jd_path)

        # Extract plain text
        resume_text = extract_text(resume_path)
        jd_text = extract_text(jd_path)

        # Keywords for demo (in real system, should be parsed from JD automatically)
        must_have = ["python", "machine learning", "sql"]
        good_to_have = ["flask", "aws", "data visualization"]

        # Compute results
        score, verdict, missing = evaluate_resume(resume_text, jd_text, must_have, good_to_have)

        return render_template(
            "results.html",
            score=score,
            verdict=verdict,
            missing=missing
        )

    # If GET request, show upload form
    return render_template("index.html")


# ---------------- Run App ---------------- #
if __name__ == "__main__":
    app.run(debug=True)
