import unittest
from unittest import mock

from src.users.application.bus.user_command_query import FindUserQuery, CreateUserCommand, UpdateUserCommand
from src.users.application.services.user_app_service import UserFinderdAppService, UserCreateAppService, \
    UserUpdateAppService
from src.users.domain.user import User
from src.users.domain.user_repository import UserFinderRepository, UserMngRepository
from sdk.exception import RepositoryNotFound


class UserMockRepository:
    @staticmethod
    def finder_ok():
        repository = mock.create_autospec(UserFinderRepository)
        repository.find_by_id.return_value = User('123', 'jose', 'guillermo')
        return repository

    @staticmethod
    def finder_error():
        repository = mock.create_autospec(UserFinderRepository)
        repository.find_by_id.return_value = None
        return repository

    @staticmethod
    def mng_ok():
        repository = mock.create_autospec(UserMngRepository)
        repository.persist.return_value = True
        return repository


class TestUserFinderService(unittest.TestCase):

    def test_user_find_by_id_ok(self):
        service = UserFinderdAppService(UserMockRepository.finder_ok())
        user = service.find_by_id('123')
        self.assertEqual('123', user['id'])

    def test_user_find_by_id_error(self):
        service = UserFinderdAppService(UserMockRepository.finder_error())
        with self.assertRaises(RepositoryNotFound):
            service.find_by_id('123')


class TestUserCreateService(unittest.TestCase):

    def test_user_create_ok(self):
        service = UserCreateAppService(UserMockRepository.mng_ok())
        status = service.create('123', 'jose', 'guillermo')
        self.assertEqual(True, status)


class TestUserUpdateService(unittest.TestCase):

    def test_user_update_ok(self):
        service = UserUpdateAppService(UserMockRepository.mng_ok(),UserMockRepository.finder_ok())
        status = service.update('123', 'jose', 'guillermo')
        self.assertEqual(True, status)

    def test_user_update_error(self):
        service = UserUpdateAppService(UserMockRepository.mng_ok(), UserMockRepository.finder_error())
        with self.assertRaises(RepositoryNotFound):
            service.update('123', 'jose', 'guillermo')

