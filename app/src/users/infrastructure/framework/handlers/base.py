# -*- coding: utf-8 -*-
import falcon

from src.users.infrastructure.bus import CommandBusSync, QueryBusSync


class Base:

    def __init__(self) -> None:
        self.command_bus = CommandBusSync()
        self.command_query = QueryBusSync()

    def print(self,value):
        print('*****************************')
        print(value)
        print('--*************************--')

    def handle_404(req, resp):
        resp.status = falcon.HTTP_404
        resp.body = 'Not found'
