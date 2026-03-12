from flask import Flask, render_template, request
import os

from config import UPLOAD_FOLDER

from utils.file_handler import save_uploaded_files

from modules.resume_parser import extract_text_from_pdf
from modules.preprocess import preprocess_text
from modules.skill_extractor import extract_skills
from modules.job_parser import parse_job_description
from modules.similarity_engine import calculate_similarity
from modules.ranking_engine import rank_candidates


app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# create uploads folder if it does not exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)



@app.route("/")
def index():
    return render_template("index.html")



@app.route("/analyze", methods=["POST"])
def analyze():

    job_description = request.form.get("job_description")

    files = request.files.getlist("resumes")

    # save uploaded resumes
    saved_files = save_uploaded_files(files, app.config["UPLOAD_FOLDER"])

    # extract job description skills
    job_skills = parse_job_description(job_description)

    results = []

    for file_path in saved_files:

        # extract text from resume
        text = extract_text_from_pdf(file_path)

        # clean text
        processed = preprocess_text(text)

        # extract skills from resume
        resume_skills = extract_skills(processed)

        # calculate similarity score
        score = calculate_similarity(job_skills, resume_skills)

        candidate = {
            "filename": os.path.basename(file_path),
            "skills": resume_skills,
            "score": score
        }

        results.append(candidate)

    # rank candidates
    ranked = rank_candidates(results)

    # -------- TERMINAL OUTPUT --------
    print("\n==============================")
    print("Candidate Scores (Terminal)")
    print("==============================")

    for candidate in ranked:

        # remove .pdf extension
        name = os.path.splitext(candidate["filename"])[0]

        score = candidate["score"]

        print(f"{name} : {score}%")

    print("==============================\n")
    # ---------------------------------

    return render_template(
        "results.html",
        candidates=ranked,
        job_skills=job_skills
    )



if __name__ == "__main__":
    app.run(debug=True)