def interview_preparation(llm, resume):

    prompt = f"""
    Generate interview questions based on this resume.

    Include:
    1. Five technical questions
    2. Five Python questions
    3. Five HR questions
    4. Sample answers

    Resume:
    {resume}
    """

    response = llm.invoke(prompt)

    return response.content