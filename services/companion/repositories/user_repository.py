from sqlmodel import Session, select

from services.companion.models.user_model import User


class UserRepository:

    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user_by_email(self, email: str):
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()

    def get_user_by_username(self, username: str):
        statement = select(User).where(User.username == username)
        return self.session.exec(statement).first()

    def get_user_by_id(self, user_id: int):
        return self.session.get(User, user_id)
    
    def get_all_users(self, session: Session):
        statement = select(User)
        return session.exec(statement).all()