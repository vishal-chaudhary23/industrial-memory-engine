from app.ingestion.parser import extract_text
from app.ingestion.chunker import chunk_text
from app.retrieval.retriever import retriever

def ingest_document(pdf_path):

    text = extract_text(pdf_path)

    chunks = chunk_text(text)

    retriever.add_texts(chunks)

    return len(chunks)