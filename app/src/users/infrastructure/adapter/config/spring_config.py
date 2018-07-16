# -*- coding: utf-8 -*-
import requests
from os import environ

from sdk.adapter.config.base import BaseConfig


class SpringConfig(BaseConfig):

    def __init__(self):
        try:
            host = environ.get('SPRING_CONFIG_SERVICES') if environ.get('SPRING_CONFIG_SERVICES') is not None else 'http://balancer'
            user = environ.get('SPRING_CONFIG_USER') if environ.get('SPRING_CONFIG_USER') is not None else 'urb'
            pwd = environ.get('SPRING_CONFIG_PASS') if environ.get('SPRING_CONFIG_PASS') is not None else 'urb'
            response = requests.get(host, auth=(user, pwd))
            data = response.json()
            database_mysql = data['database']['mysql']
            self._config = {
                'database': {
                    'host': database_mysql['host'],
                    'db': database_mysql['dbname'],
                    'user': database_mysql['user'],
                    'pwd': database_mysql['password'],
                    'port': database_mysql['port'],
                },
                'services': {
                    'host_base' : data['api_microservices_host'],
                    'rest': {
                        'ms_location': data['ms_location'],
                        'ms_user': data['ms_user']
                    }
                },
                'aws': data['aws']
            }
        except Exception as e:
            raise e
