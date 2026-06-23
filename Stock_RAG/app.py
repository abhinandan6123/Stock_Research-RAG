"""
app.py  —  Stock Research RAG
Free stack: HuggingFace embeddings + ChromaDB + Groq (Llama 3)
"""
from pathlib import Path
from ingest import ingest
import os
import streamlit as st
from pathlib import Path
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# ── Config ────────────────────────────────────────────────────────────────────
CHROMA_DIR = "chroma_db"
TOP_K = 3

PROMPT_TEMPLATE = """You are a stock research analyst assistant.
Use ONLY the context provided below to answer the question.
If the answer is not found in the context, say: "This is not covered in the research notes."
Be concise, factual, and specific. No speculation beyond what the notes state.

Context:
{context}

Question: {question}

Answer:"""

# ── Page setup ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Stock Research RAG", page_icon="📈", layout="wide")

st.markdown("""
<style>
    .block-container { padding-top: 1.8rem; max-width: 820px; }
    .answer-box {
        background: #f9fafb;
        border-left: 4px solid #2563eb;
        padding: 1rem 1.2rem;
        border-radius: 0 6px 6px 0;
        font-size: 0.95rem;
        line-height: 1.7;
        margin-top: 0.8rem;
    }
    .source-card {
        background: #fff;
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        padding: 0.65rem 0.9rem;
        margin-bottom: 0.5rem;
        font-size: 0.82rem;
        color: #374151;
    }
    .source-label {
        font-weight: 600;
        color: #1d4ed8;
        margin-bottom: 0.3rem;
    }
    .meta { font-size: 0.78rem; color: #9ca3af; margin-bottom: 1.2rem; }
</style>
""", unsafe_allow_html=True)

st.title("📈 Stock Research RAG")
st.markdown(
    '<p class="meta">Knowledge base: Obsidian-style markdown · '
    'Embeddings: all-MiniLM-L6-v2 (free) · '
    'Vector DB: ChromaDB · '
    'LLM: Llama 3 via Groq (free)</p>',
    unsafe_allow_html=True,
)

# ── Sidebar: API key ──────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Configuration")
    groq_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="gsk_…",
        help="Free at console.groq.com",
    )
    st.caption("Get a free key at [console.groq.com](https://console.groq.com)")
    st.divider()
    st.markdown("**Stack**")
    st.markdown("- Embeddings: `all-MiniLM-L6-v2`")
    st.markdown("- Vector DB: ChromaDB (local)")
    st.markdown("- LLM: `llama3-8b-8192` via Groq")
    st.markdown("- Retrieval: top-3 chunks")
    st.markdown("- Cost: **$0.00**")

if not groq_key:
    st.info("Enter your Groq API key in the sidebar to start. It's free at console.groq.com")
    st.stop()

# ── Load ChromaDB ─────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner="Loading vector store…")
def load_vectorstore():

    if not Path(CHROMA_DIR).exists():
        with st.spinner("Building vector database for first run..."):
            ingest()

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
    )

    return Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings,
    )

@st.cache_resource(show_spinner=False)
def build_chain(_vectorstore, api_key: str):
    llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=api_key,
)
    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["context", "question"],
    )
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=_vectorstore.as_retriever(search_kwargs={"k": TOP_K}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
    )


vectorstore = load_vectorstore()
collection = vectorstore._collection
n_chunks = collection.count()
st.metric("Chunks indexed", n_chunks)

st.divider()

# ── Sample questions ──────────────────────────────────────────────────────────
SAMPLES = [
    "AI supply chain bottlenecks",
    "What is NVIDIA's competitive moat?",
    "Which stocks benefit from AI capex?",
    "What are the risks in semiconductor sector?",
    "How does TSMC impact AI chip supply?",
    "What is Broadcom's custom ASIC business?",
]

st.markdown("**Try a sample question:**")
cols = st.columns(3)
chosen = None
for i, q in enumerate(SAMPLES):
    if cols[i % 3].button(q, key=f"q{i}", use_container_width=True):
        chosen = q

query = st.text_input(
    "Or type your own question",
    value=chosen or "",
    placeholder="e.g. AI supply chain bottlenecks",
)

# ── Query ─────────────────────────────────────────────────────────────────────
if query:
    with st.spinner("Searching knowledge base…"):
        try:
            chain = build_chain(vectorstore, groq_key)
            result = chain.invoke({"query": query})
        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

    st.markdown("### Answer")
    st.markdown(
        f'<div class="answer-box">{result["result"]}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("### Sources used")
    for doc in result["source_documents"]:
        source = Path(doc.metadata.get("source", "unknown")).stem.replace("_", " ").title()
        preview = doc.page_content[:280].strip()
        st.markdown(
            f'<div class="source-card">'
            f'<div class="source-label">📄 {source}</div>'
            f'{preview}…'
            f'</div>',
            unsafe_allow_html=True,
        )
