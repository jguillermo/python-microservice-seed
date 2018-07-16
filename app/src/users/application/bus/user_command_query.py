from sdk.bus import Command, Query


class FindUserQuery(Query):
    def __init__(self, id):
        self.id = id


class CreateUserCommand(Command):
    def __init__(self, id, name, last_name):
        self.id = id
        self.name = name
        self.last_name = last_name


class UpdateUserCommand(Command):
    def __init__(self, id, name, last_name):
        self.id = id
        self.name = name
        self.last_name = last_name
