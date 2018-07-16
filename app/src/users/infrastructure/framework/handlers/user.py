# -*- coding: utf-8 -*-
import falcon

from bootstrap.container import AdapterInjector
from bootstrap.framework.decorators.service import handler_except
from src.users.application.bus.user_command_query import CreateUserCommand, UpdateUserCommand, FindUserQuery
from sdk.types import TypeUuid
from src.users.infrastructure.framework.handlers.base import Base


class UserHandler(Base):

    @handler_except
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        id = TypeUuid.random().value()
        command = CreateUserCommand(
            id=id,
            name=req.media.get('name'),
            last_name=req.media.get('last_name'))

        self.command_bus.dispatch(command)

        return {'id': id}

    @handler_except
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        filter = req.params.get('last_name')  # type: str

        # TODO: falta refactorizar
        sql = " SELECT * FROM user where last_name='{}' LIMIT 1".format(filter)
        return AdapterInjector.sql_search().result(sql)


class UserIdHandler(Base):

    @handler_except
    def on_get(self, req: falcon.Request, resp: falcon.Response, id):
        query = FindUserQuery(id)
        return self.command_query.ask(query)

    @handler_except
    def on_put(self, req: falcon.Request, resp: falcon.Response, id):
        command = UpdateUserCommand(
            id=id,
            name=req.media.get('name'),
            last_name=req.media.get('last_name'))
        self.command_bus.dispatch(command)
        return 'ok'
