import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

# from tests.utils.docker_utils import create_database_container
from tests.utils.db_utils import upgrade_db

from app.middlewares import auth_middleware


@pytest.fixture(scope="session", autouse=True)
def create_database():
    # container = create_database_container()
    print("Container has been setup for the tests")

    # create db connection
    print("TEST DB URL!!!", os.environ.get("DB_URL_TEST"))
    engine = create_engine(url=os.environ.get("DB_URL_TEST"))

    # create a transactional connection
    with engine.begin() as transaction_connection:
        upgrade_db(transaction_connection, "head")

    SESSIONLOCAL = sessionmaker(bind=engine, autoflush=True, autocommit=False)
    yield SESSIONLOCAL

    # Delete container once the all the tests are complete
    # container.stop()
    # container.remove()


def mock_fake_authorize():
    print("Mock fake_authorize is called")
    return lambda func: func


@pytest.fixture(scope="function")
def client(monkeypatch):
    print("Setting up test client & patching")
    monkeypatch.setattr(auth_middleware, "auth_requests", mock_fake_authorize())

    from app.main import app

    with TestClient(app=app) as client:
        yield client
