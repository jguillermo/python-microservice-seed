from sdk.types import TypeUuid, TypeString, TypeBase, TypeInteger


class UserId(TypeUuid):
    pass


class UserName(TypeString):
    def validate(self, value_name=''):
        super().validate('Nombre de usuario')
        if self.is_required() and self._value.__len__() < 3:
            raise Exception("El nombre debe ser mayor a 2 caracteres")


class UserLastName(TypeString):
    def __init__(self, value: str):
        super().__init__(value, False)

    def validate(self, value_name=''):
        super().validate('Apellido')
        if self.is_not_none() and self._value.__len__() < 4:
            raise Exception("El apellido debe ser mayor a 3 caracteres")


class UserYear(TypeInteger):
    def validate(self, value_name=''):
        super().validate()
        if self.is_required() and self._value < 0:
            raise Exception("la edad tiene que ser mayor que cero")


class User:
    def __init__(self, id, name, last_name):
        self.id = id
        self.name = name
        self.last_name = last_name


class UserFactory:
    @staticmethod
    def create(id, name, last_name) -> User:
        id = UserId(id)
        name = UserName(name)
        last_name = UserLastName(last_name)
        UserFactory._validate([id, name, last_name])
        return User(id.value(), name.value(), last_name.value())

    @staticmethod
    def _validate(value_object):
        for vo in value_object:  # type: TypeBase
            vo.validate()
