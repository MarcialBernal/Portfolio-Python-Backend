from fastapi import FastAPI
from fastapi.testclient import TestClient

from services.companion.routers import routes as companion_routes


app = FastAPI()
app.include_router(companion_routes.router)
client = TestClient(app)


def test_chat_returns_answer(monkeypatch):
    def fake_answer(question: str) -> str:
        assert question == "Explain the Warehouse project"
        return "The Warehouse project manages inventory."

    monkeypatch.setattr(companion_routes.companion, "answer", fake_answer)

    response = client.post(
        "/chat",
        json={"question": "Explain the Warehouse project"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "answer": "The Warehouse project manages inventory."
    }


def test_chat_rejects_empty_question():
    response = client.post("/chat", json={"question": ""})

    assert response.status_code == 422