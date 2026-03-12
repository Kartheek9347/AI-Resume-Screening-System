from modules.preprocess import preprocess_text
from modules.skill_extractor import extract_skills


def parse_job_description(job_description):

    processed = preprocess_text(job_description)

    job_skills = extract_skills(processed)

    return job_skills