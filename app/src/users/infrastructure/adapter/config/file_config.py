# -*- coding: utf-8 -*-

from os import environ
from sdk.adapter.config.base import BaseConfig


class FileConfig(BaseConfig):

    def __init__(self):
        try:

            # self._validate('DATABASE')
            database_url = environ.get('DATABASE')

            self._config = {
                'database': {
                    'url': database_url
                },
                'services': {
                    'host_base': '',
                    'rest': {
                        'ms_location': '',
                        'ms_user': ''
                    }
                },
                'aws': {
                    's3': 'lll'
                }
            }
        except Exception as e:
            print(str(e))
            raise e

    def _validate(self,value):
        if environ.get(value) is not None:
            raise Exception('No existe la variable: {}'.format(value))
