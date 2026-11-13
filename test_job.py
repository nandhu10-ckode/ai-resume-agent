from llm import llm
from agents.job_agent import job_recommender

resume = """
Education: BSc Artificial Intelligence and Machine Learning

Skills:
Python, SQL, Pandas, NumPy,
Machine Learning, NLP

Projects:
Sentiment Analysis using NLP

Experience:
Fresher
"""

result = job_recommender(llm, resume)

print("\nJOB RECOMMENDATIONS")
print(result)