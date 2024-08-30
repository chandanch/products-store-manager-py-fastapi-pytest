from sqlalchemy import Integer, String, Boolean, Text, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID

TABLE_NAME = "product"


def test_model_structure_product_table_exists(db_inspector):
    assert db_inspector.has_table(TABLE_NAME)


def test_model_structure_product_column_types(db_inspector):
    columns = {
        columns["name"]: columns for columns in db_inspector.get_columns(TABLE_NAME)
    }

    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["pid"]["type"], UUID)
    assert isinstance(columns["name"]["type"], String)
    assert isinstance(columns["slug"]["type"], String)
    assert isinstance(columns["description"]["type"], Text)
    assert isinstance(columns["is_digital"]["type"], Boolean)
    assert isinstance(columns["created_at"]["type"], DateTime)
    assert isinstance(columns["updated_at"]["type"], DateTime)
    assert isinstance(columns["is_active"]["type"], Boolean)
    assert isinstance(columns["stock_status"]["type"], Enum)
    assert isinstance(columns["category_id"]["type"], Integer)
    assert isinstance(columns["seasonal_event"]["type"], Integer)


def test_model_structure_product_nullable_constraints(db_inspector):
    columns = db_inspector.get_columns(TABLE_NAME)

    expected_nullable_columns = {
        "id": False,
        "pid": False,
        "name": False,
        "slug": False,
        "description": True,
        "is_digital": False,
        "created_at": False,
        "updated_at": False,
        "is_active": False,
        "stock_status": False,
        "category_id": False,
        "seasonal_event": True,
    }

    for column in columns:
        # print(f"Column: {column}")
        # Raise assertion error with an optional error message
        assert column["nullable"] == expected_nullable_columns.get(
            column["name"]
        ), f"Column '{column['name']}' cannot be null"


def test_model_structure_product_column_constraints(db_inspector):
    constraints = db_inspector.get_check_constraints(TABLE_NAME)

    for constraint in constraints:
        assert any(constraint["name"] == "product_name_length_constraint")
        assert any(constraint["name"] == "product_slug_length_constraint")


def test_model_structure_product_default_values(db_inspector):
    columns = {
        columns["name"]: columns for columns in db_inspector.get_columns(TABLE_NAME)
    }
    # print(columns)
    assert columns["is_digital"]["default"] == "false"
    assert columns["is_active"]["default"] == "false"
    assert columns["stock_status"]["default"] == "'oos'::status_enum"


def test_model_structure_product_column_lengths(db_inspector):
    columns = {
        columns["name"]: columns for columns in db_inspector.get_columns(TABLE_NAME)
    }
    # print(columns)
    assert columns["name"]["type"].length == 200
    assert columns["slug"]["type"].length == 220


def test_model_strcuture_product_unique_constraints(db_inspector):
    constraints = db_inspector.get_unique_constraints(TABLE_NAME)
    # print("Test Constraints...", constraints)

    assert any(
        constraint["name"] == "unq_product_name_constraint"
        for constraint in constraints
    )
    assert any(
        constraint["name"] == "unq_product_slug_constraint"
        for constraint in constraints
    )
