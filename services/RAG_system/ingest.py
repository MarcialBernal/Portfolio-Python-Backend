from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


BASE_DIR = Path(__file__).resolve().parent
DOC_PATH = str(BASE_DIR / "DOC")
PERSIST_DIR = str(BASE_DIR / "chroma_db")


def ingest_documents():
    # 1. Leer todos los archivos Markdown
    loader = DirectoryLoader(
        DOC_PATH,
        glob="**/*.md",
        loader_cls=TextLoader
    )

    documents = loader.load()

    # 2. Dividir los documentos en fragmentos
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    # 3. Convertir los fragmentos en embeddings
    embeddings = OpenAIEmbeddings()

    # 4. Guardarlos en Chroma
    Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=PERSIST_DIR
    )

    print("Knowledge base created.")
    return True


if __name__ == "__main__":
    ingest_documents()