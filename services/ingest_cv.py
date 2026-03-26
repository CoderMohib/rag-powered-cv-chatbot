import os
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()

def ingest_data_to_mongodb():
    # 1. Configuration from .env
    mongo_uri = os.getenv("MONGODB_URI")
    db_name = os.getenv("MONGODB_DB_NAME")
    collection_name = os.getenv("MONGODB_COLLECTION_NAME")
    
    if not mongo_uri or not os.getenv("GOOGLE_API_KEY"):
        print("Error: Please check your .env file for MONGODB_URI and GOOGLE_API_KEY")
        return

    # 2. Connect to MongoDB
    client = MongoClient(mongo_uri)
    collection = client[db_name][collection_name]

    # 3. Setup Embeddings (Gemini)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

    # 4. Check if data already exists to avoid duplicates
    if collection.count_documents({}) > 0:
        print(f"--- Data already exists in {collection_name}. Skipping ingestion. ---")
    else:
        print("--- Loading PDF ---")
        # Ensure your CV filename matches this
        loader = PyPDFLoader("my_cv.pdf") 
        data = loader.load()

        print("--- Splitting text into chunks ---")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, 
            chunk_overlap=50
        )
        docs = text_splitter.split_documents(data)

        print(f"--- Uploading {len(docs)} chunks to MongoDB Atlas ---")
        MongoDBAtlasVectorSearch.from_documents(
            documents=docs,
            embedding=embeddings,
            collection=collection,
            index_name=os.getenv("MONGODB_VECTOR_INDEX_NAME")
        )
        print("--- Ingestion Complete! ---")

    client.close()

if __name__ == "__main__":
    ingest_data_to_mongodb()