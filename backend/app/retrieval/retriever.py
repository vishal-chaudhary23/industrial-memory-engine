from langchain_community.retrievers import PineconeHybridSearchRetriever
# from langchain_community.retrievers.pinecone_hybrid_search import PineconeHybridSearchRetriever
# from langchain_community.retrievers.pinecone_hybrid_search
from app.ingestion.embeddings import embeddings
from app.vectorstore.pinecone_store import index
from pinecone_text.sparse import BM25Encoder

bm25_encoder = BM25Encoder.default()

retriever = PineconeHybridSearchRetriever(
    embeddings=embeddings,
    sparse_encoder=bm25_encoder,
    index=index
)
# def search(query, top_k=5):
#     query_vector = embeddings.embed_query(query)

#     results = index.query(
#         vector=query_vector,
#         top_k=top_k,
#         include_metadata=True
#     )

#     return results