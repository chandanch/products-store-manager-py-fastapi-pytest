import pytest

from tests.utils.docker_utils import create_database_container


@pytest.fixture(scope="session", autouse=True)
def create_database():
    create_database_container()
    print("Container has been setup for the tests")
