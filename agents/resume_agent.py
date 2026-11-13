def resume_analyzer(llm, resume):

    prompt = f"""
    Analyse this resume.

    Find:
    1. Education
    2. Skills
    3. Projects
    4. Experience
    5. Strengths

    Resume:
    {resume}
    """

    response = llm.invoke(prompt)

    return response.content