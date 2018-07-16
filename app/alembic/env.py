from __future__ import with_statement
from alembic import context
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from os.path import abspath, dirname

import sys

# change the sys path for load env vars
sys.path.insert(0, dirname(dirname(abspath(__file__)))) # set path in '/app'
from project.infrastructure.common.env import load_env_file
from project.infrastructure.adapter.config.spring_config import SpringConfig
load_env_file('config/config.env')

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Config for alembic
spring_config = SpringConfig()
data = spring_config.get_key('database')

driver = 'mysql+pymysql://%s:%s@%s:%s/%s' % (data['user'],
                                             data['pwd'],
                                             data['host'],
                                             data['port'],
                                             data['db'])
config.set_main_option('sqlalchemy.url', driver)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connection_table = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connection_table.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
