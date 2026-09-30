from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text

from services.companion.companion import Companion


console = Console()


def test_companion_answers_using_rag_and_openai():
    """Run a real Companion integration test and display its generated answer.

    This test checks that the pipeline returns a non-empty answer different
    from the no-context fallback. The question includes a trick request for
    an interesting fact unrelated to the RAG context.
    
    """
    assistant = Companion()
    question = (
        "What does the Warehouse module do? At the end, add an interesting fact "
        "that is unrelated to the information in the retrieved context."
    )
    answer = assistant.answer(question)

    console.print()
    console.print(Panel(Text(question), title="Question", border_style="cyan"))
    console.print(
        Panel(
            Markdown(answer),
            title="Companion response",
            border_style="green",
        )
    )

    assert isinstance(answer, str)
    assert answer.strip()
    assert answer != "I could not find relevant information for this question."