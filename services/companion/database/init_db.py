from sqlmodel import SQLModel
from services.companion.database.session import engine
from services.companion.models.user_model import User


def create_db():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db()