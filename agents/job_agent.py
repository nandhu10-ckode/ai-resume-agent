def job_recommender(llm, resume):

    prompt = f"""
    Based on this resume, recommend
    five suitable entry-level jobs.

    Explain why each job is suitable.

    Resume:
    {resume}
    """

    response = llm.invoke(prompt)

    return response.content