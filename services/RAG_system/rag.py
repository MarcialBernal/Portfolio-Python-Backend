from pathlib import Path
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
PERSIST_DIR = str(BASE_DIR / "chroma_db")

embeddings = OpenAIEmbeddings()

db = Chroma(
    persist_directory=PERSIST_DIR,
    embedding_function=embeddings
)


def ask_rag(user_message: str):
    results = db.similarity_search(user_message, k=3)
    return results

# Y desde el asistente, harías algo como:
# context = ask_rag(user_message)
# response = build_answer(user_message, context)