from models.model_router import invoke_with_fallback
from langchain_core.messages import HumanMessage

conversation_memory = []

def should_summarize(user_input, response):
    if len(user_input.split()) < 4:
        return False
    if len(response.split()) < 20:
        return False

    ignore_words = ["hi", "hello", "ok", "thanks", "bye"]
    if user_input.lower() in ignore_words:
        return False

    return True


def summarize_interaction(user_input, response):
    prompt = f"""
    Summarize this interaction in 1 short line.

    User: {user_input}
    Assistant: {response}

    Summary:
    """

    result = invoke_with_fallback([HumanMessage(content=prompt)])
    return result.content.strip()


def update_memory(user_input, response):
    if not should_summarize(user_input, response):
        return

    summary = summarize_interaction(user_input, response)
    conversation_memory.append(summary)

    if len(conversation_memory) > 5:
        conversation_memory.pop(0)


def get_memory():
    return "\n".join(conversation_memory)