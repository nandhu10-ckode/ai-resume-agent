from agents.ats_agent import ats_analyzer

resume = """
BSc Artificial Intelligence

Skills:
Python, SQL, Pandas, NumPy,
Machine Learning, NLP

Projects:
Sentiment Analysis using NLP
"""

job_description = """
We are looking for a fresher.

Required skills:
Python, SQL, Machine Learning,
Deep Learning, Pandas, Communication.
"""

result = ats_analyzer(resume, job_description)

print("\nATS ANALYSIS")

print("ATS Score:", result["score"], "/100")

print("Matched Skills:", result["matched"])

print("Missing Skills:", result["missing"])