from fastapi import FastAPI
from app.api.upload import router
from app.api.search import router as search_router
from app.api.chat import router as chat_router



app = FastAPI()

app.include_router(router)
app.include_router(search_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "Industrial Memory Engine"}