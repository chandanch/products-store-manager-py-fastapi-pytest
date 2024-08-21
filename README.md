# Product Store Manager

A Simple Store manager app for managing products, built with Python & FastAPI

## Application Setup & Run

1. Install dependencies: `pipenv install`
2. Activate virtual env: `pipenv shell`
3. Start the service: `./run_startup.sh`

## Alembic Commands

### Intialize Alembic Version

`alembic init migrations`

The command `alembic init migrations` is used to initialize a new Alembic environment in your project. This command sets up the necessary directory structure and configuration files that Alembic needs to manage database migrations.

## Generate Migration Version

`alembic revision --autogenerate -m "<message>"`

This command is used to generate a new migration revision/version

## Generate Migration Version For Named Configuration

`alembic -n <config_name> revision --autogenerate -m "<message>"`

This command is used to generate a new migration revision/version for a named configurartion. The named configuration will be specified in the alembic.ini file

## Update Migration in Database

`alembic upgrade head`

The command is used to apply all pending database migrations up to the latest version

## Update Migration in Database For a Named Configuration

`alembic -n <config_name> upgrade head`

The command is used to apply all pending database migrations up to the latest version in the context of a specific named configuration.
