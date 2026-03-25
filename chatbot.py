from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()
checkPointer = InMemorySaver()
model = init_chat_model(
    "gemini-2.5-flash", model_provider="google_genai", temperature=0
)

agent = create_agent(
    model=model,
    checkpointer=checkPointer,
    system_prompt="You are a helpful assistant. Keep answers short, clear, and to the point (max 3-4 lines)."
)


while True:
    user_input = input("👤 You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Chat closed!")
        break

    response = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config={"configurable": {"thread_id": "user_1"}},
    )
    print("🤖 AI:", response["messages"][-1].content.strip())
