from abc import ABC, abstractmethod
from src.users.domain.user import User


class UserMngRepository(ABC):
    @abstractmethod
    def persist(self, user: User) -> bool:
        pass


class UserFinderRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: str) -> User:
        pass


class UserSearchRepository(ABC):
    @abstractmethod
    def listAll(self, filter):
        pass
