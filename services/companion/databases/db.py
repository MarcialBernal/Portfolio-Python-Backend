import os
from sqlmodel import SQLModel, create_engine
from backend.services.companion.models import user_models

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

sqlite_url = f"sqlite:///{db_path}"
connect_args = {"check_same_thread": False}

engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
    print("DB creada en:", db_path)