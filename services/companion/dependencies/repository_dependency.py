from services.companion.repositories.user_repository import UserRepository


def get_user_repository(session):
    return UserRepository(session)