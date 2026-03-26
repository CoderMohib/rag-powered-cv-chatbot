from langchain_core.messages import HumanMessage, SystemMessage
from models.model_router import invoke_with_fallback
from rag.query import smart_query, cached_retrieval
from rag.context_builder import build_context
from memory.memory_manager import update_memory, get_memory
from prompts.system_prompt import SYSTEM_PROMPT


def ask_cv(user_input):
    better_query = smart_query(user_input)
    docs = list(cached_retrieval(better_query))

    if not docs:
        return "I couldn't find relevant information in the CV."

    context = build_context(docs)
    memory_context = get_memory()

    response = invoke_with_fallback([
        SystemMessage(
            content=SYSTEM_PROMPT.format(
                context=context,
                question=user_input
            ) + f"\n\n🧠 Conversation Context:\n{memory_context}"
        ),
        HumanMessage(content=user_input)
    ])

    final_answer = response.content

    update_memory(user_input, final_answer)

    return final_answer