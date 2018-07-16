from src.users.application.bus.user_command_query import UpdateUserCommand, CreateUserCommand, FindUserQuery
from src.users.domain.user import UserFactory, UserName, UserLastName
from src.users.domain.user_repository import UserFinderRepository, UserMngRepository
from src.users.domain.user_service import UserFinderService


class UserFinderdAppService:
    def __init__(self, user_finder_repository: UserFinderRepository):
        self.user_finder_service = UserFinderService(user_finder_repository)

    def find_by_id(self, id):
        user = self.user_finder_service.find_by_id(id)
        return {
            'id': user.id,
            'name': user.name,
            'last_name': user.last_name
        }


class UserCreateAppService:
    def __init__(self, user_mng_repository: UserMngRepository):
        self.user_mng_repository = user_mng_repository

    def create(self, id, name, last_name):
        user = UserFactory.create(id, name, last_name)
        self.user_mng_repository.persist(user)
        return True


class UserUpdateAppService:
    def __init__(self, user_mng_repository: UserMngRepository, user_finder_repository: UserFinderRepository):
        self.user_mng_repository = user_mng_repository
        self.user_finder_service = UserFinderService(user_finder_repository)

    def update(self, id, name, last_name):
        user = self.user_finder_service.find_by_id(id)

        vo_name = UserName(name)
        vo_last_name = UserLastName(last_name)

        vo_name.validate()
        vo_last_name.validate()

        user.name = vo_name.value()
        user.last_name = vo_last_name.value()
        self.user_mng_repository.persist(user)
        return True
