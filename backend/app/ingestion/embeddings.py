from langchain_huggingface import HuggingFaceEmbeddings
import os 
from dotenv import load_dotenv

load_dotenv()
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

embeddings = HuggingFaceEmbeddings(
    model_name='all-MiniLM-L6-v2'
    # model_name="BAAI/bge-small-en-v1.5"
    # model_name="BAAI/bge-m3"
)

# vector = embeddings.embed_query("hello")
# print(len(vector))