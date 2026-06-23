from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import ask_question

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/chat")
def chat(request: QueryRequest):

    results = ask_question(
        request.query
    )

    return results