from functools import lru_cache
from models.model_router import invoke_with_fallback
from langchain_core.messages import HumanMessage
from rag.retriever import retriever


@lru_cache(maxsize=100)
def cached_retrieval(query):
    return tuple(retriever.invoke(query))


def rewrite_query(query):
    prompt = f"""
    Rewrite this query for CV retrieval:

    Query: {query}
    """

    result = invoke_with_fallback([HumanMessage(content=prompt)])
    return result.content.strip()


def smart_query(query):
    if len(query.split()) < 3:
        return rewrite_query(query)
    return query