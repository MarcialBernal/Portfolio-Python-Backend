from services.RAG_system.rag import ask_rag


def test_ask_rag_returns_documents():
    question = "¿How does the Warehouse project work?"

    results = ask_rag(question)

    print(f"\nQuestion: {question}")
    print(f"Results found: {len(results)}")

    for index, document in enumerate(results, start=1):
        print(f"\n--- Result {index} ---")
        print(document.page_content)

    assert len(results) > 0

    for document in results:
        assert document.page_content