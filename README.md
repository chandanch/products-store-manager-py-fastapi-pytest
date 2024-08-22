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

## Database Structural Testing

The database structurual testing verifies the integrity and correctness of the database schemas and its associated structures such as tables columns contraints, foriegn keys etc. in a database.

### Table & Column Validation

- Confirm the presence of all required tables within the database schema.

- Validate the existence of expected columns in each table, ensuring correct data types.

- Verify nullable or not nullable fields

- Test columns with specific constraints to ensure they are accurately defined.

- Verify the correctness of default values for relevant columns.

- Ensure that column lengths align with defined requirements.

### Schema Testing

_To be added_

### Index Testing

_To be added_
