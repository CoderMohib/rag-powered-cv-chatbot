import os
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.tools import Tool
from langgraph.checkpoint.memory import InMemorySaver

# 1. Load Environment & Setup MongoDB
load_dotenv()

def get_cv_tool():
    client = MongoClient(os.getenv("MONGODB_URI"))
    collection = client[os.getenv("MONGODB_DB_NAME")][os.getenv("MONGODB_COLLECTION_NAME")]
    
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    
    vector_store = MongoDBAtlasVectorSearch(
        collection=collection,
        embedding=embeddings,
        index_name=os.getenv("MONGODB_VECTOR_INDEX_NAME")
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    return Tool(
        name="search_cv",
        func=lambda query: retriever.invoke(query),
        description="Search CV for skills, experience, education"
    )

# 2. Initialize Components
checkPointer = InMemorySaver()
model = init_chat_model(
    "gemini-2.0-flash", # Use 2.0-flash for stable tool-calling
    model_provider="google_genai", 
    temperature=0
)

# 3. Create Agent with the CV Tool
agent = create_agent(
    model=model,
    tools=[get_cv_tool()], # Added the MongoDB tool here
    checkpointer=checkPointer,
    system_prompt="You are a helpful career assistant. Use the search_cv tool to answer questions about the candidate's background. Keep answers short and clear."
)

# 4. Chat Loop
while True:
    user_input = input("👤 You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Chat closed!")
        break

    response = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config={"configurable": {"thread_id": "user_1"}},
    )
    
    # Print the last message in the sequence
    print("🤖 AI:", response["messages"][-1].content.strip())