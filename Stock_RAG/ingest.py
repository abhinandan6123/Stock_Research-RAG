"""
ingest.py
Run once to build the ChromaDB vector store from markdown files.
Usage: python ingest.py
"""

from pathlib import Path

from langchain_community.document_loaders import (
    DirectoryLoader,
    UnstructuredMarkdownLoader,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Base directory (works locally, Colab, and Streamlit Cloud)
BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"
CHROMA_DIR = BASE_DIR / "chroma_db"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


def ingest():
    print("Loading markdown files...")

    if not DATA_DIR.exists():
        raise FileNotFoundError(
            f"Data directory not found: {DATA_DIR}"
        )

    loader = DirectoryLoader(
        str(DATA_DIR),
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader,
    )

    docs = loader.load()
    print(f"  Loaded {len(docs)} documents")

    print("Chunking documents...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n## ", "\n### ", "\n\n", "\n", " "],
    )

    chunks = splitter.split_documents(docs)
    print(f"  Created {len(chunks)} chunks")

    print("Loading embedding model (all-MiniLM-L6-v2)...")

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
    )

    print("Building ChromaDB vector store...")

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
    )

    vectordb.persist()

    print(f"  Vector store saved to {CHROMA_DIR}")
    print("Ingestion complete.")


if __name__ == "__main__":
    ingest()
    print(f"  Vector store saved to ./{CHROMA_DIR}/")
    print("Ingestion complete.")


if __name__ == "__main__":
    ingest()
