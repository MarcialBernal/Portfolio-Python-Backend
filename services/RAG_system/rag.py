from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


embeddings = OpenAIEmbeddings()

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)


def ask_rag(user_message: str):
    question = user_message
    results = db.similarity_search(question, k=3)
    return results

# Y desde el asistente, harías algo como:
# context = ask_rag(user_message)
# response = build_answer(user_message, context)