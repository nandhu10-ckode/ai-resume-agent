def career_roadmap(llm, skill_gaps):

    prompt = f"""
    Create a beginner-friendly learning roadmap.

    Include:
    1. Topics to learn
    2. Weekly learning plan
    3. Practical exercises
    4. Projects
    5. Interview preparation

    Skill gaps:
    {skill_gaps}
    """

    response = llm.invoke(prompt)

    return response.content