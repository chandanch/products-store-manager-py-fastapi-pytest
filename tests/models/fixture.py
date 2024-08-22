import pytest
from sqlalchemy import inspect


@pytest.fixture(scope="function")
def inspect_database(db_session):
    return inspect(db_session.bind())
