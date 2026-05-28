from langchain_text_splitters import RecursiveCharacterTextSplitter

def dividir_documentos(documentos):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_documents(documentos)