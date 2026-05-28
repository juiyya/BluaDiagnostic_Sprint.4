from rag.vectorstore import obter_vectorstore

def obter_retriever():

    db = obter_vectorstore()
    return db.as_retriever(search_kwargs={"k": 3})