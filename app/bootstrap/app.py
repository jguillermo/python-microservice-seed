# -*- coding: utf-8 -*-
from bootstrap.framework import FalconApi
from src.users.infrastructure.repository.sqlalchemy.mapping import load_mapper
from sdk.env import load_env_file


class App:
    def __init__(self):
        load_env_file('config/config.env')
        load_mapper()
        self.api = FalconApi().api
