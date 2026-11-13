from llm import llm
from agents.skill_gap_agent import skill_gap_analyzer

resume = """
Education: BSc Artificial Intelligence

Skills:
Python, SQL, Pandas, NumPy

Projects:
Sentiment Analysis using NLP

Experience:
Fresher
"""

job_description = """
Required skills:
Python, SQL, Machine Learning,
Deep Learning, TensorFlow, NLP,
Communication and Data Analysis.
"""

result = skill_gap_analyzer(
    llm,
    resume,
    job_description
)

print("\nSKILL GAP ANALYSIS")
print(result)