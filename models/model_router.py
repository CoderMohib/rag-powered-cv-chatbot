from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
import time
from dotenv import load_dotenv

load_dotenv()

# =========================
# 🔹 Initialize Models
# =========================

# Gemini Models
gemini_flash = init_chat_model(
    "gemini-2.0-flash", model_provider="google_genai", temperature=0
)

gemini_pro = init_chat_model(
    "gemini-2.5-pro", model_provider="google_genai", temperature=0
)

# Groq Models
groq_fast = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

groq_strong = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)


# =========================
# 🔹 Model List (Order Matters)
# =========================

MODEL_CHAIN = [
    ("groq_fast", groq_fast),
    ("groq_strong", groq_strong),
    ("gemini_flash", gemini_flash),
    ("gemini_pro", gemini_pro),
]


# =========================
# 🔹 Fallback Logic
# =========================


def invoke_with_fallback(messages, max_retries_per_model=2):
    """
    Tries each model with retry logic.
    Each model gets 'max_retries_per_model' attempts.
    """

    last_error = None

    for model_name, model in MODEL_CHAIN:
        for attempt in range(max_retries_per_model):
            try:
                # print(f"⚡ {model_name} | Attempt {attempt + 1}")

                response = model.invoke(messages)

                # Safety check (sometimes empty response happens)
                if response and hasattr(response, "content") and response.content:
                    return response

            except Exception as e:
                # print(f"❌ {model_name} failed (Attempt {attempt + 1}): {e}")
                last_error = e
                time.sleep(1)

        # print(f"🚫 Skipping {model_name} after {max_retries_per_model} attempts\n")

    raise Exception(f"All models failed. Last error: {last_error}")
