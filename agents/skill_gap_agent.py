def skill_gap_analyzer(llm, resume, job_description):

    prompt = f"""
    Compare the resume with the job description.

    Identify:
    1. Existing skills
    2. Missing skills
    3. Skills to improve
    4. Suggested projects

    Resume:
    {resume}

    Job Description:
    {job_description}
    """

    response = llm.invoke(prompt)

    return response.content