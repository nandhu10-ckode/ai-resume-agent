from llm import llm
from agents.roadmap_agent import career_roadmap

skill_gaps = """
Existing Skills:
Python, SQL, Pandas, NumPy.

Skills to improve:
Machine Learning, Deep Learning,
TensorFlow, NLP.

Projects to practise:
Chatbot using NLP.
Image classification using CNN.
"""

result = career_roadmap(llm, skill_gaps)

print("\nCAREER LEARNING ROADMAP")
print(result)