import pytest
from sqlalchemy import inspect


@pytest.fixture(scope="function")
def db_inspector(create_database):
    db_session = create_database
    return inspect(db_session().bind)
