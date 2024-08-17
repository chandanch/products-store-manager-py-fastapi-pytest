import docker
from docker.errors import NotFound
import time


def check_container_exists(client, container_name: SyntaxError) -> bool:

    try:
        container = client.containers.get(container_name)
        return True, container
    except NotFound:
        return False, None


def is_container_running(container) -> bool:
    container.reload()
    return container.status == "running"


def create_database_container():
    client = docker.from_env()
    CONTAINER_NAME = "test-db"
    is_container_exists, existing_container = check_container_exists(
        client, CONTAINER_NAME
    )

    if is_container_exists:
        print(f"Container with name {CONTAINER_NAME} already exists")
        print(f"Deleting Container {CONTAINER_NAME}")
        existing_container.stop()
        existing_container.remove()
        print(f"Existing Container {CONTAINER_NAME} has been deleted")

    container_config = {
        "name": CONTAINER_NAME,
        "image": "postgres:16.4-alpine3.20",
        "detach": True,
        "ports": {"5432": "5434"},
        "environment": {
            "POSTGRES_USER": "postgres",
            "POSTGRES_PASSWORD": "prodtesterstore123",
            "POSTGRES_DB": "productstore",
        },
    }
    container = client.containers.run(**container_config)

    print("Checking container health..")

    elapse_count = 0
    while not is_container_running(container):
        elapse_count += 1
        if elapse_count == 10:
            raise RuntimeError("Container did not start in expected time")
        time.sleep(1)

    is_container_started = is_container_running(container)

    if is_container_started:
        return container
    else:
        raise RuntimeError("Container did not start, check for errors")
