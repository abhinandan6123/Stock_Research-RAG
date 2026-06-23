# Stock Research RAG

A production-style Retrieval-Augmented Generation (RAG) application for stock research, built using local embeddings, ChromaDB vector search, and Groq-hosted Llama 3.1. The system enables natural-language querying across structured investment research notes while maintaining source transparency, low latency, and near-zero operating cost.

---

## Live Demo

**Application:** https://stockresearch-rag-aa3daeunai9qeqtpwihgjv.streamlit.app/

**GitHub Repository:** https://github.com/abhinandan6123/Stock_Research-RAG

---

## Overview

This project demonstrates a cost-efficient RAG pipeline for financial research.

Instead of relying on expensive hosted vector databases or paid embedding APIs, the application uses:

* Local sentence-transformer embeddings
* ChromaDB for persistent vector storage
* Groq-hosted Llama 3.1 for low-latency inference
* Markdown-based knowledge management
* Streamlit for rapid deployment

The result is a lightweight stock research assistant capable of answering questions grounded in curated research notes.

---

## Key Features

### Semantic Search

Search across research documents using vector similarity rather than keyword matching.

### Retrieval-Augmented Generation

Relevant context is retrieved before generation, reducing hallucinations and improving factual accuracy.

### Source Attribution

Every answer includes the supporting documents used during retrieval.

### Cost-Efficient Architecture

Uses local embeddings and a free Groq inference endpoint to minimize operational costs.

### Extensible Knowledge Base

New research notes can be added simply by dropping markdown files into the data directory.

---

## System Architecture

```text
Research Notes (.md)
        │
        ▼
Recursive Chunking
(500 chars, 50 overlap)
        │
        ▼
Embeddings
(all-MiniLM-L6-v2)
        │
        ▼
ChromaDB
(Vector Store)
        │
        ▼
Top-K Retrieval
(k = 3)
        │
        ▼
Groq Llama 3.1 8B Instant
        │
        ▼
Streamlit Interface
```

### Retrieval Flow

1. User submits a question.
2. Query is converted into an embedding.
3. ChromaDB retrieves the most relevant chunks.
4. Retrieved context is injected into the prompt.
5. Llama 3.1 generates a grounded response.
6. Supporting sources are displayed.

---

## Technical Decisions

| Component       | Technology                     | Rationale                                      |
| --------------- | ------------------------------ | ---------------------------------------------- |
| Embeddings      | all-MiniLM-L6-v2               | Lightweight, free, strong semantic performance |
| Vector Database | ChromaDB                       | Persistent local vector storage                |
| LLM             | Llama 3.1 8B Instant (Groq)    | Fast inference with no infrastructure overhead |
| Chunking        | RecursiveCharacterTextSplitter | Preserves semantic structure                   |
| Retrieval       | Top-K = 3                      | Balances accuracy and token efficiency         |
| Frontend        | Streamlit                      | Rapid deployment and demonstration             |

---

## Knowledge Base

The system currently indexes eight research notes covering major AI infrastructure and semiconductor companies:

| Company / Topic    | Coverage                                  |
| ------------------ | ----------------------------------------- |
| NVIDIA             | Competitive moat, Blackwell, AI ecosystem |
| TSMC               | Foundry dominance, CoWoS bottlenecks      |
| AMD                | MI300X, GPU competition                   |
| Broadcom           | Custom ASIC strategy                      |
| ASML               | EUV monopoly and supply chain leverage    |
| Microsoft          | Azure AI and OpenAI ecosystem             |
| AI CapEx Trends    | Infrastructure spending trends            |
| Supply Chain Risks | Semiconductor bottlenecks and constraints |

---

## Sample Questions

* What is NVIDIA's competitive moat?
* Which companies benefit most from AI infrastructure spending?
* How does TSMC influence AI chip supply?
* What are the major semiconductor supply chain bottlenecks?
* What role does ASML play in the AI ecosystem?
* What is Broadcom's custom ASIC business?

---

## Installation

### Clone Repository

```bash
git clone https://github.com/abhinandan6123/Stock_Research-RAG.git
cd Stock_Research-RAG
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Application

```bash
streamlit run app.py
```

### Configure API Key

Create a free API key from:

https://console.groq.com

Enter the key in the Streamlit sidebar when prompted.

---

## Deployment

The application is deployed using Streamlit Community Cloud.

Deployment steps:

1. Push repository to GitHub
2. Connect repository to Streamlit Cloud
3. Set app entry point
4. Deploy

The vector database is automatically generated during first launch if not already present.

---

## Future Improvements

* Hybrid retrieval (BM25 + Vector Search)
* Reranking pipeline
* Portfolio analysis mode
* Earnings call ingestion
* PDF research ingestion
* Multi-document citation support
* Agentic research workflows

---

## Author

**Venkata Abhinandan Kancharla**

AI & Machine Learning Engineer

Portfolio: https://abhikancharla.vercel.app

GitHub: https://github.com/abhinandan6123

LinkedIn: https://www.linkedin.com/in/abhikancharla

---

## License

This project is released under the MIT License.
