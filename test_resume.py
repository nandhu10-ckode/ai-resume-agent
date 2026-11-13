from llm import llm
from agents.resume_agent import resume_analyzer

resume = """
Education: BSc Artificial Intelligence and Machine Learning

Skills:
Python, SQL, Machine Learning, Pandas, NumPy

Projects:
Sentiment Analysis using NLP
AI Career Assistant

Experience:
Fresher
"""

result = resume_analyzer(llm, resume)

print("\nRESUME ANALYSIS")
print(result)