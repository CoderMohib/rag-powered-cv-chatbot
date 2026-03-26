def build_context(docs, max_chars=3000):
    context = ""

    for doc in docs:
        section = doc.metadata.get("section", "General")
        chunk = f"[{section}]\n{doc.page_content}\n\n"

        if len(context) + len(chunk) > max_chars:
            break

        context += chunk

    return context