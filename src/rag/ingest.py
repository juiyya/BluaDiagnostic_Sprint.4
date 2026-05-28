import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from rag.chunking import dividir_documentos
from rag.vectorstore import obter_vectorstore

def inicializar_e_injetar_base():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    kb_dir = os.path.abspath(os.path.join(base_dir, "..", "..", "data", "knowledge_base"))
    
    print(f"[RAG] Carregando documentos de: {kb_dir}")
 
    loader = DirectoryLoader(kb_dir, glob="*.md", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
    documentos = loader.load()
    
    if not documentos:
        print("[RAG] Nenhum documento encontrado para ingestão.")
        return
        
    print(f"[RAG] Total de documentos carregados: {len(documentos)}")
    
    chunks = dividir_documentos(documentos)
    print(f"[RAG] Documentos divididos em {len(chunks)} chunks.")
    
    db = obter_vectorstore()
    db.add_documents(chunks)
    print("[RAG] Ingestão concluída e dados persistidos no Chroma DB.")

if __name__ == "__main__":
    inicializar_e_injetar_base()