import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langsmith import traceable

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

@traceable(name="Groq LLM")
def generate_response(prompt):
    return llm.invoke(prompt).content