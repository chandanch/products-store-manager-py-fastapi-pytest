import alembic.config
from alembic import command


def upgrade_db(connection=None, revision="head"):

    # setup alembic config path and get the config
    config = alembic.config.Config("alembic.ini")
    if connection is not None:
        # specify the configuration to used by alembic
        config.config_ini_section = "testdb"
        # upgrade db using 'command'
        print(f"Migrating Test DB to revision {revision}")
        command.upgrade(config=config, revision=revision)
