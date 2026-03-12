def calculate_similarity(job_skills, resume_skills):

    if not job_skills:
        return 0

    matched = set(job_skills).intersection(set(resume_skills))

    score = len(matched) / len(job_skills)

    percentage = round(score * 100, 2)

    return percentage