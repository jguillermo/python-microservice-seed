from sqlalchemy import Table, Column, String, CHAR, MetaData
from sqlalchemy.orm import mapper, clear_mappers
from src.users.domain.user import User

metadata = MetaData()

user = Table('user', metadata,
             Column('id', CHAR(36), primary_key=True),
             Column('name', String(50)),
             Column('last_name', String(50)),
             )


def load_mapper():
    print("inicio el mapper!!!!!!!!!!!!")
    clear_mappers()
    mapper(User, user)
