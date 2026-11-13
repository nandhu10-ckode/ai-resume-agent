from llm import llm

from agents.interview_agent import interview_preparation


resume = """
Education: BSc Artificial Intelligence and Machine Learning

Skills:
Python, SQL, Pandas, NumPy,
Machine Learning, NLP

Projects:
Sentiment Analysis using NLP
AI Career Assistant

Experience:
Fresher
"""


result = interview_preparation(llm, resume)

print("\nAI INTERVIEW PREPARATION")

print(result)