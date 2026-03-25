# import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
# from langchain.messages import HumanMessage, AIMessage, SystemMessage
# from langchain.tools import tool
from pydantic import BaseModel, Field
load_dotenv()

model = init_chat_model("google_genai:gemini-2.5-flash-lite")

# conversation = [
#     {"role": "system", "content": "You are a helpful assistant that translates English to French."},
#     {"role": "user", "content": "Translate: I love programming."},
#     {"role": "assistant", "content": "J'adore la programmation."},
#     {"role": "user", "content": "Translate: I love building applications."}
# ]
# conversation = [
#     SystemMessage("You are a helpful assistant that translates English to French."),
#     HumanMessage("Translate: I love programming."),
#     AIMessage("J'adore la programmation."),
#     HumanMessage("Translate: I love building applications.")
# ]

# response = model.invoke(conversation)
# print(response)  # AIMessage("J'adore créer des applications.")

# full = None  # None | AIMessageChunk
# for chunk in model.stream("What color is the sky?"):
#     full = chunk if full is None else full + chunk
#     print(full.text)

# The
# The sky
# The sky is
# The sky is typically
# The sky is typically blue
# ...

# print(full.content_blocks)
# [{"type": "text", "text": "The sky is typically blue..."}]

# responses = model.batch(
#     [
#         "Why do parrots have colorful feathers?",
#         "How do airplanes fly?",
#         "What is quantum computing?",
#     ],
#     config={
#         "max_concurrency": 2,  # Limit to 5 parallel calls
#     },
# )
# for response in responses:
#     print(response)
# @tool
# def get_weather(location: str) -> str:
#     """Get the weather at a location."""
#     return f"It's sunny in {location}."

# # Bind (potentially multiple) tools to the model
# model_with_tools = model.bind_tools([get_weather])

# # Step 1: Model generates tool calls
# messages = [{"role": "user", "content": "What's the weather in Boston?"}]
# ai_msg = model_with_tools.invoke(messages)
# messages.append(ai_msg)

# # Step 2: Execute tools and collect results
# for tool_call in ai_msg.tool_calls:
#     # Execute the tool with the generated arguments
#     tool_result = get_weather.invoke(tool_call)
#     messages.append(tool_result)

# # Step 3: Pass results back to model for final response
# final_response = model_with_tools.invoke(messages)
# print(final_response.text)
# "The current weather in Boston is 72°F and sunny."


class Actor(BaseModel):
    name: str
    role: str

class MovieDetails(BaseModel):
    title: str
    year: int
    cast: list[Actor]
    genres: list[str]
    budget: float | None = Field(None, description="Budget in millions USD")

model_with_structure = model.with_structured_output(MovieDetails)

response = model_with_structure.invoke("Provide details about the movie Inception")
print(response)  # Movie(title="Inception", year=2010, director="Christopher Nolan", rating=8.8)