def ats_analyzer(resume, job_description):

    skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "pandas",
        "numpy",
        "nlp",
        "communication"
    ]

    resume = resume.lower()
    job_description = job_description.lower()

    required_skills = [
        skill for skill in skills
        if skill in job_description
    ]

    matched_skills = [
        skill for skill in required_skills
        if skill in resume
    ]

    if required_skills:
        score = int(
            len(matched_skills) / len(required_skills) * 100
        )
    else:
        score = 0

    return {
        "score": score,
        "matched": matched_skills,
        "missing": [
            skill for skill in required_skills
            if skill not in matched_skills
        ]
    }