from fastapi import APIRouter
from pydantic import BaseModel
from app.retrieval.retriever import retriever

router = APIRouter()

class Query(BaseModel):
    query: str

@router.post("/search")
def search(data: Query):

    docs = retriever.invoke(
        data.query
    )

    return {
        "results": [
            doc.page_content
            for doc in docs
        ]
    }