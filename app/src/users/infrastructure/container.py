# -*- coding: utf-8 -*-
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from bootstrap.container import AdapterInjector
from src.users.application.bus.user_handler import FindUserQueryHandler, CreateUserCommandHandler, \
    UpdateUserCommandHandler
from src.users.application.services.doc import DocumentationAppService
from src.users.application.services.user_app_service import UserFinderdAppService, UserCreateAppService, \
    UserUpdateAppService
from src.users.infrastructure.repository.sqlalchemy.user import UserSqlMngRepository, UserSqlFinderRepository


class RepositoryInjector(containers.DeclarativeContainer):
    """
    Repository
    """
    user_mng = providers.Singleton(UserSqlMngRepository, adapter=AdapterInjector.sql_alchemy)
    user_finder = providers.Singleton(UserSqlFinderRepository, adapter=AdapterInjector.sql_alchemy)


class AppServicesInjector(containers.DeclarativeContainer):
    """
    Application Services
    """
    doc = providers.Singleton(DocumentationAppService)
    user_finder = providers.Singleton(UserFinderdAppService, user_finder_repository=RepositoryInjector.user_finder)
    user_create = providers.Singleton(UserCreateAppService, user_mng_repository=RepositoryInjector.user_mng)
    user_update = providers.Singleton(UserUpdateAppService, user_mng_repository=RepositoryInjector.user_mng,
                                      user_finder_repository=RepositoryInjector.user_finder)


class HandlerInjector(containers.DeclarativeContainer):
    """
    Handler
    """
    FindUserQuery = providers.Singleton(FindUserQueryHandler, service=AppServicesInjector.user_finder)
    CreateUserCommand = providers.Singleton(CreateUserCommandHandler, service=AppServicesInjector.user_create)
    UpdateUserCommand = providers.Singleton(UpdateUserCommandHandler, service=AppServicesInjector.user_update)
