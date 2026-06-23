# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)
from langchain_core.prompts import ChatPromptTemplate
import os

from app.retrieval.retriever import retriever
from app.services.llm import llm

# load_dotenv()

# llm = ChatGroq(
#     model="llama-3.3-70b-versatile",
#     groq_api_key=os.getenv("GROQ_API_KEY")
# )

prompt = ChatPromptTemplate.from_template("""
You are an Industrial Intelligence Assistant.

Use only the provided context.

Context:
{context}

Question:
{input}
""")

question_answer_chain = create_stuff_documents_chain(
    llm,
    prompt
)

rag_chain = create_retrieval_chain(
    retriever,
    question_answer_chain
)

def ask_question(query: str):

    response = rag_chain.invoke({
        "input": query
    })

    return response["answer"]

print("hi")