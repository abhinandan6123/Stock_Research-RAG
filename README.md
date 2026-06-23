# Stock_Research-RAG
Cost-efficient RAG system for stock research using markdown knowledge bases, semantic search, ChromaDB, local embeddings, and Streamlit deployment.

---

## Interface

![Stock Research RAG UI](assets/demo.png)

### Features
- 🔍 **Semantic search** across 8 stock research notes
- 💬 **Natural language queries** — ask like you're talking to an analyst
- 📄 **Source transparency** — see exactly which notes were used to answer
- ⚡ **Fast retrieval** — Groq's Llama 3 responds in under 2 seconds
- 💰 **Zero cost** — local embeddings + free Groq API

---

## Architecture

```
Markdown Files (data/)
        ↓
   Chunking (500 tokens, 50 overlap)
        ↓
   Embeddings (all-MiniLM-L6-v2, local)
        ↓
   ChromaDB (local vector store)
        ↓
   Retriever (top-3 chunks)
        ↓
   LLM (Llama 3 8B via Groq — free)
        ↓
   Streamlit UI
```

---

## Why These Choices

| Decision | Choice | Reason |
|----------|--------|--------|
| Embeddings | `all-MiniLM-L6-v2` | Free, runs locally, good semantic accuracy |
| Vector DB | ChromaDB | No external service, persists to disk |
| LLM | Llama 3 8B (Groq) | Free API, fast (300 tok/s), no cost |
| Chunk size | 500 tokens | Enough context per chunk, avoids large context windows |
| Top-K | 3 | Sufficient retrieval, minimal token usage |
| Splitter | `RecursiveCharacterTextSplitter` | Respects markdown headers → semantic chunks |

**Cost per query: $0.00**

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/abhi6123/stock-research-rag.git
cd stock-research-rag
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get a free Groq API key
Go to [console.groq.com](https://console.groq.com) → Create account → API Keys → Create key

### 4. Build the vector store (run once)
```bash
python ingest.py
```

### 5. Run the app
```bash
streamlit run app.py
```

Open `http://localhost:8501` — enter your Groq API key in the sidebar and start querying.

---

## Docker

```bash
docker build -t stock-rag .
docker run -p 8501:8501 stock-rag
```

---

## Deploy to Streamlit Cloud (Free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo → set `app.py` as entry point
4. Add secret: `GROQ_API_KEY = gsk_...` (optional, or enter at runtime)
5. Deploy → get a public URL

---

## Knowledge Base

8 research notes in `data/`:

| File | Coverage |
|------|----------|
| `nvidia.md` | NVDA business, bottlenecks, Blackwell, financials |
| `tsmc.md` | Foundry role, CoWoS constraint, geopolitical risk |
| `amd.md` | MI300X, ROCm gap, supply chain |
| `broadcom.md` | Custom ASICs, hyperscaler XPUs, VMware |
| `asml.md` | EUV monopoly, export controls, pricing |
| `microsoft.md` | Azure AI, OpenAI partnership, Copilot |
| `ai_capex_trends.md` | $200B hyperscaler spend, beneficiary layers |
| `supply_chain_risks.md` | HBM shortage, packaging, power, geopolitics |

To add more notes: drop any `.md` file into `data/` and re-run `python ingest.py`.

---

## Sample Questions

- AI supply chain bottlenecks
- What is NVIDIA's competitive moat?
- Which stocks benefit from AI capex spending?
- How does TSMC impact AI chip supply?
- What are the risks in the semiconductor sector?
- What is Broadcom's custom ASIC business?

---

## Project Structure

```
stock-research-rag/
├── app.py                  ← Streamlit UI
├── ingest.py               ← Build vector store (run once)
├── requirements.txt
├── Dockerfile
├── README.md
└── data/                   ← Obsidian-style markdown knowledge base
    ├── nvidia.md
    ├── tsmc.md
    ├── amd.md
    ├── broadcom.md
    ├── asml.md
    ├── microsoft.md
    ├── ai_capex_trends.md
    └── supply_chain_risks.md
```

---

## Built By

**Venkata Abhinandan Kancharla** — AI Engineer

[![Portfolio](https://img.shields.io/badge/Portfolio-abhikancharla.vercel.app-blue?style=flat&logo=vercel)](https://abhikancharla.vercel.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-abhi6123-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/abhi6123)
