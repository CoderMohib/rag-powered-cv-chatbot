# 💼 CV Assistant — RAG-based AI Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot that answers questions about a candidate's CV using **LangChain**, **MongoDB Atlas Vector Search**, and **Google Gemini / Groq LLMs** — all from a simple terminal interface.

---

## 🧠 How It Works

```
User Question
     │
     ▼
Smart Query Rewriter       ← rewrites short/vague queries using LLM
     │
     ▼
MongoDB Atlas Vector Search  ← retrieves top-k relevant CV chunks (MMR)
     │
     ▼
Context Builder             ← formats retrieved docs into clean context
     │
     ▼
System Prompt + Memory      ← injects context + conversation history
     │
     ▼
LLM with Fallback Chain     ← Groq (fast) → Groq (strong) → Gemini Flash → Gemini Pro
     │
     ▼
Final Answer  →  Memory Updated  →  User
```

---

## ✨ Features

- 📄 **PDF Ingestion** — Loads and chunks your CV from a PDF file
- 🔍 **Semantic Search** — Uses Gemini embeddings + MongoDB Atlas Vector Search (MMR retrieval)
- 🧠 **Conversation Memory** — Summarizes and retains the last 5 interactions
- 🔄 **Smart Query Rewriting** — Expands short queries before retrieval
- ⚡ **LLM Fallback Chain** — Automatically falls back across 4 models if one fails
- 🚀 **Caching** — `lru_cache` prevents redundant retrieval calls for repeated queries

---

## 🗂️ Project Structure

```
LangChain/
│
├── main.py                    # Entry point — terminal chat loop
│
├── services/
│   ├── cv_service.py          # Core RAG pipeline (query → retrieve → respond)
│   └── ingest_cv.py           # One-time CV ingestion script into MongoDB
│
├── rag/
│   ├── retriever.py           # MongoDB Atlas Vector Search retriever setup
│   ├── query.py               # Smart query rewriting + cached retrieval
│   └── context_builder.py     # Formats retrieved docs into prompt context
│
├── models/
│   └── model_router.py        # Multi-model fallback chain (Groq + Gemini)
│
├── memory/
│   └── memory_manager.py      # Summarized conversation memory (last 5 turns)
│
├── prompts/
│   └── system_prompt.py       # Structured system prompt for the CV assistant
│
├── my_cv.pdf                  # Your CV file (ingested once into MongoDB)
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables (not committed)
```

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd LangChain
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
# or
source .venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key

MONGODB_URI=your_mongodb_atlas_connection_string
MONGODB_DB_NAME=your_database_name
MONGODB_COLLECTION_NAME=your_collection_name
MONGODB_VECTOR_INDEX_NAME=your_vector_index_name
```

> **Get API Keys:**
> - Google AI (Gemini): https://aistudio.google.com/app/apikey
> - Groq: https://console.groq.com/keys
> - MongoDB Atlas: https://cloud.mongodb.com

### 5. Set Up MongoDB Atlas Vector Index

In your MongoDB Atlas cluster, create a **Vector Search Index** on your collection with the following configuration:

```json
{
  "fields": [
    {
      "type": "vector",
      "path": "embedding",
      "numDimensions": 3072,
      "similarity": "cosine"
    }
  ]
}
```

> The index name must match `MONGODB_VECTOR_INDEX_NAME` in your `.env`.

---

## 🚀 Usage

### Step 1: Ingest Your CV (Run Once)

Place your CV as `my_cv.pdf` in the project root, then run:

```bash
python services/ingest_cv.py
```

This will:
1. Load and split the PDF into chunks (500 chars, 50 overlap)
2. Generate Gemini embeddings for each chunk
3. Upload all chunks to MongoDB Atlas

> ✅ Safe to re-run — skips ingestion if data already exists.

### Step 2: Start the Chat

```bash
python main.py
```

```
💼 CV Assistant — type 'exit' to quit

👤 You: What programming languages does the candidate know?
🤖 AI: Based on the CV, the candidate is proficient in...

👤 You: exit
👋 Chat closed!
```

---

## 🤖 Model Fallback Chain

The system automatically tries models in this order, retrying each up to 2 times:

| Priority | Model | Provider | Speed |
|----------|-------|----------|-------|
| 1 | `llama-3.1-8b-instant` | Groq | ⚡ Fastest |
| 2 | `llama-3.1-70b-versatile` | Groq | 🔥 Strong |
| 3 | `gemini-2.0-flash` | Google | 🌟 Balanced |
| 4 | `gemini-2.5-pro` | Google | 🧠 Most capable |

---

## 📦 Key Dependencies

| Package | Purpose |
|---------|---------|
| `langchain` | Core RAG framework |
| `langchain-mongodb` | MongoDB Atlas Vector Search integration |
| `langchain-google-genai` | Gemini embeddings & LLM |
| `langchain-groq` | Groq LLM integration |
| `langchain-community` | PDF document loader |
| `pymongo` | MongoDB client |
| `python-dotenv` | Environment variable management |

---

## 🔒 Environment & Security

- **Never commit** your `.env` file — it's listed in `.gitignore`
- Keep your API keys secure and rotate them if exposed
- `my_cv.pdf` is also excluded from version control by default

---

## 📝 License

This project is for personal and educational use.
