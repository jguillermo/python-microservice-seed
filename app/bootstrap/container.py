# -*- coding: utf-8 -*-
import dependency_injector.containers as containers
import dependency_injector.providers as providers
from src.users.infrastructure.adapter.config.file_config import FileConfig
from sdk.adapter.log.logging import ConsoleLogger
from sdk.adapter.sql.sqlalchemy import SqlAlchemyAdapter, SqlAlchemySearchAdapter


class LoggerInjector(containers.DeclarativeContainer):
    console = providers.Singleton(ConsoleLogger)


class ConfigInjector(containers.DeclarativeContainer):
    app_config = providers.Singleton(FileConfig)


class AdapterInjector(containers.DeclarativeContainer):
    """
    Adapter
    """
    # sql_alchemy_session = providers.Singleton(SqlAlchemySession, config=ConfigInjector.app_config)
    sql_alchemy = providers.Factory(SqlAlchemyAdapter)
    sql_search = providers.Factory(SqlAlchemySearchAdapter)  # type: SqlAlchemySearchAdapter()


