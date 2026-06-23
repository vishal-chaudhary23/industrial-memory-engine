from fastapi import APIRouter, UploadFile, File
import os
from app.ingestion.parser import extract_text
from app.services.ingest_service import ingest_document


router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    chunks = ingest_document(file_path)

    return {
        "filename": file.filename,
        "chunks": chunks
    }