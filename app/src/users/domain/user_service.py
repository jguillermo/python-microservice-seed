from src.users.domain.user import User
from src.users.domain.user_repository import UserFinderRepository
from sdk.exception import RepositoryNotFound


class UserFinderService:
    def __init__(self, user_finder_repository: UserFinderRepository) -> None:
        self._user_finder_repository = user_finder_repository

    def find_by_id(self, id: str) -> User:
        user = self._user_finder_repository.find_by_id(id)
        self._guard(id, user)
        return user

    def _guard(self, id, user):
        if user is None:
            raise RepositoryNotFound("No existe el usuario con id : " + id)
