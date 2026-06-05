from sqlmodel import Session

from services.companion.repositories.user_repository import UserRepository


def get_users(session: Session):
    repository = UserRepository(session)
    return repository.get_all_users(session)