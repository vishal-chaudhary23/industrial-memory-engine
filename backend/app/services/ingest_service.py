from app.ingestion.parser import extract_text
from app.ingestion.chunker import chunk_text
from app.retrieval.retriever import retriever
from app.graph.entity_extractor import extract_entities
from app.graph.neo4j_store import save_graph
import os


def ingest_document(pdf_path):

    text = extract_text(pdf_path)

    chunks = chunk_text(text)

    metadatas = []

    filename = os.path.basename(pdf_path)
    for _ in chunks:
        metadatas.append({
            "source": filename
        })

    # # Pinecone
    retriever.add_texts(
        texts=chunks,
        metadatas=metadatas
    )
    # retriever.add_texts(chunks)

    # Neo4j
    for chunk in chunks:

        data = extract_entities(chunk)

        save_graph(data, filename)


    return len(chunks)