from fastapi import Depends
from sqlmodel import Session, select
from services.companion.models.user_model import User


class UserRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(User)
        return self.session.exec(statement).all()