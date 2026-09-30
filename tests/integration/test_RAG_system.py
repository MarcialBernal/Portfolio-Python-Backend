from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from services.RAG_system.rag import ask_rag


console = Console()


def test_ask_rag_returns_documents():
    """Verify that the RAG system retrieves and displays non-empty documents.

    The test checks that at least one document is returned and that each
    retrieved document contains content. It does not verify the relevance
    or correctness of the retrieved information.
    """
    question = "How does the Warehouse project work?"
    results = ask_rag(question)

    console.print()
    console.print(Panel(question, title="RAG query", border_style="cyan"))
    console.print(f"[bold]Results found:[/bold] {len(results)}")

    for index, document in enumerate(results, start=1):
        console.print(
            Panel(
                Markdown(document.page_content),
                title=f"Retrieved document {index}",
                border_style="green",
            )
        )

    assert results

    for document in results:
        assert document.page_content.strip()