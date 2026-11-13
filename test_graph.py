from graph import career_graph

resume = """
Education: BSc Artificial Intelligence and Machine Learning

Skills:
Python, SQL, Pandas, NumPy, Machine Learning, NLP

Projects:
Sentiment Analysis using NLP

Experience:
Fresher
"""

job_description = """
Looking for a fresher with Python, SQL,
Machine Learning, Deep Learning and communication skills.
"""

result = career_graph.invoke({
    "resume": resume,
    "job_description": job_description
})

print("\nRESUME ANALYSIS")
print(result["analysis"])

print("\nATS RESULT")
print(result["ats"])

print("\nJOB RECOMMENDATIONS")
print(result["jobs"])

print("\nSKILL GAP")
print(result["gaps"])

print("\nCAREER ROADMAP")
print(result["roadmap"])

print("\nINTERVIEW PREPARATION")
print(result["interview"])