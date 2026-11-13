from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(
    model=os.getenv("GROQ_MODEL"),
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)