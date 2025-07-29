from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEndpointEmbeddings  # ✅ use updated class
import os
from flipkart.data_converter import dataconverter
from dotenv import load_dotenv

# Load env vars
load_dotenv()

# Get secrets
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
HF_TOKEN = os.getenv("HF_TOKEN")


# ✅ Use updated embeddings
embedding = HuggingFaceEndpointEmbeddings(
    huggingfacehub_api_token=HF_TOKEN,
    model="sentence-transformers/all-MiniLM-L6-v2"
)


def data_ingestion(status):
    vstore = AstraDBVectorStore(
        embedding=embedding,
        collection_name="flipkart",
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE
    )

    if status is None:
        docs = dataconverter()
        insert_ids = vstore.add_documents(docs)
        return vstore, insert_ids
    else:
        return vstore, []

if __name__ == "__main__":
    vstore, insert_ids = data_ingestion(None)
    print(f"\nInserted {len(insert_ids)} documents.")
    results = vstore.similarity_search("Can you tell me the low budget sound basshead?")
    for res in results:
        print(f"\n{res.page_content} [{res.metadata}]")
