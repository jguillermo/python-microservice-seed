from src.users.application.bus.user_command_query import CreateUserCommand, UpdateUserCommand, FindUserQuery
from src.users.application.services.user_app_service import UserCreateAppService, UserUpdateAppService, \
    UserFinderdAppService
from sdk.bus import Handler


class FindUserQueryHandler(Handler):
    def __init__(self, service: UserFinderdAppService):
        self.service = service

    def handle(self, query: FindUserQuery):
        return self.service.find_by_id(query.id)


class CreateUserCommandHandler(Handler):

    def __init__(self, service: UserCreateAppService):
        self.service = service

    def handle(self, command: CreateUserCommand):
        self.service.create(command.id, command.name, command.last_name)


class UpdateUserCommandHandler(Handler):
    def __init__(self, service: UserUpdateAppService):
        self.service = service

    def handle(self, command: UpdateUserCommand):
        self.service.update(command.id, command.name, command.last_name)
