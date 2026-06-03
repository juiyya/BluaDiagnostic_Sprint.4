import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

def obter_embeddings():
    return OllamaEmbeddings(model="nomic-embed-text")

def obter_vectorstore():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    persist_dir = os.path.abspath(os.path.join(base_dir, "..", "..", "data", "chroma_db"))
    
    embeddings = obter_embeddings()
    return Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings,
        collection_name="diretrizes_careplus"
    )