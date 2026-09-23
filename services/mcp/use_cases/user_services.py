from services.companion.dependencies.repository_dependency import get_user_repository


class UserService:

    def get_all_users(self, session):
        repository = get_user_repository(session)
        return repository.get_all()