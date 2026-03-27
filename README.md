# 💼 AI Portfolio Assistant — RAG-powered Chatbot

A professional, high-end **Retrieval-Augmented Generation (RAG)** chatbot designed to act as an "AI Twin" for your portfolio. Built with **LangChain**, **Streamlit**, and **MongoDB Atlas**, it allows recruiters to interactively explore your CV, projects, and skills through a sleek, modern web interface.

---

## 🚀 Live Demo
**Check it out here:** [mohib-info.streamlit.app](https://mohib-info.streamlit.app)

---

## ✨ Key Features

- 🎨 **Premium UI/UX** — Modern "Dark Mode" aesthetic with electric blue gradients and custom CSS.
- 🤖 **Smart AI Twin** — Professionally refined system prompts that handle greetings and CV-specific queries naturally.
- ⚡ **Multi-Model Fallback** — Advanced failover logic ensuring 100% uptime by cycling through **Groq (Llama 3.1)** and **Google Gemini** models.
- 🔍 **Vector Search (MMR)** — Uses **MongoDB Atlas Vector Search** with Gemini embeddings and **Max Marginal Relevance (MMR)** for the most relevant context retrieval.
- 🧠 **Smart Memory** — Automatically manages conversation history to handle follow-up questions effectively.
- � **Personal Branding** — Integrated profile card with custom circular image and social links (GitHub, LinkedIn, Email).

---

## 🛠️ Tech Stack

- **Framework:** [LangChain](https://www.langchain.com/)
- **Frontend:** [Streamlit](https://streamlit.io/) (Custom CSS + Material Symbols)
- **Database:** [MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-vector-search) (Vector Search)
- **LLMs (Fallback Chain):**
    1. `llama-3.1-8b-instant` (Groq)
    2. `llama-3.1-70b-versatile` (Groq)
    3. `gemini-2.0-flash` (Google)
    4. `gemini-2.5-pro` (Google)
- **Embeddings:** `models/gemini-embedding-001` (Google Generative AI)

---

## ⚙️ Setup & Installation

### 1. Installation
```bash
git clone https://github.com/CoderMohib/rag-powered-cv-chatbot.git
cd rag-powered-cv-chatbot
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Configuration (`.env`)
Create a `.env` file in the root directory with your specific credentials:
```env
# 🔑 API Keys
GOOGLE_API_KEY=your_google_key
GROQ_API_KEY=your_groq_key
OPENAI_API_KEY=your_openai_key

# 🍃 MongoDB Atlas Configuration
MONGODB_URI=your_mongodb_connection_string
MONGODB_DB_NAME=cv_chatbot_db
MONGODB_COLLECTION_NAME=cv_vectors
MONGODB_VECTOR_INDEX_NAME=vector_index
```

### 3. Data Ingestion
Place your CV as `my_cv.pdf` in the root folder and run the ingestion script:
```bash
python services/ingest_cv.py
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 🌐 Deployment

### Streamlit Community Cloud (Recommended)
1. **GitHub**: Push your code to a GitHub repository (ensure `.env` is ignored by `.gitignore`).
2. **Deploy**: Connect your repo to [Streamlit Cloud](https://share.streamlit.io/).
3. **Secrets**: Go to **Advanced Settings -> Secrets** and paste your `.env` variables there.
4. **Clean UI**: The `.streamlit/config.toml` is pre-configured with `toolbarMode = "minimal"` to hide dev buttons for a professional look.

---

## 🗂️ Project Structure

```text
LangChain/
├── app.py                 # Main Web UI (Streamlit)
├── services/
│   ├── cv_service.py      # Core RAG orchestration
│   └── ingest_cv.py       # Data parsing & vector ingestion
├── rag/
│   ├── retriever.py       # MongoDB Vector Search & Embeddings setup
│   ├── query.py           # Query rewriting & lru_cache retrieval
│   └── context_builder.py # Context formatting logic
├── models/
│   └── model_router.py    # Multi-LLM fallback & retry logic
├── prompts/
│   └── system_prompt.py   # AI Assistant behavioral instructions
├── assets/                # Profile image & branding assets
└── requirements.txt       # Python dependencies
```

---

## 👨‍💻 Contact

**Mohib Ali**
- **LinkedIn:** [mohib-ali-80b19b294](https://www.linkedin.com/in/mohib-ali-80b19b294/)
- **GitHub:** [@CoderMohib](https://github.com/CoderMohib)
- **Email:** alimohib025@gmail.com

---
*Developed with ❤️ using LangChain and Streamlit*
