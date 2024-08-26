from sqlalchemy import Integer, String, Boolean


TABLE_NAME = "category"


def test_model_structure_category_table_exists(db_inspector):
    assert db_inspector.has_table("category")


def test_model_structure_category_column_types(db_inspector):
    columns = {
        columns["name"]: columns for columns in db_inspector.get_columns(TABLE_NAME)
    }

    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["name"]["type"], String)
    assert isinstance(columns["slug"]["type"], String)
    assert isinstance(columns["is_active"]["type"], Boolean)
    assert isinstance(columns["level"]["type"], Integer)
    assert isinstance(columns["parent_id"]["type"], Integer)

    # print(columns)


def test_model_structure_category_nullable_constraints(db_inspector):
    columns = db_inspector.get_columns(TABLE_NAME)

    expected_nullable_columns = {
        "id": False,
        "name": False,
        "slug": False,
        "is_active": False,
        "level": False,
        "parent_id": True,
    }

    for column in columns:
        # print(f"Column: {column}")
        # Raise assertion error with an optional error message
        assert column["nullable"] == expected_nullable_columns.get(
            column["name"]
        ), f"Column '{column['name']}' cannot be null"


def test_model_structure_category_column_constraints(db_inspector):
    constraints = db_inspector.get_check_constraints(TABLE_NAME)

    for constraint in constraints:
        assert any(constraint["name"] == "name_length_constraint")
        assert any(constraint["name"] == "slug_length_constraint")


def test_model_structure_category_default_values(db_inspector):
    columns = {
        columns["name"]: columns for columns in db_inspector.get_columns(TABLE_NAME)
    }
    # print(columns)
    assert columns["is_active"]["default"] == "false"
    assert columns["level"]["default"] == "100"


def test_model_structure_category_column_lengths(db_inspector):
    columns = {
        columns["name"]: columns for columns in db_inspector.get_columns(TABLE_NAME)
    }
    # print(columns)
    assert columns["name"]["type"].length == 100
    assert columns["slug"]["type"].length == 140


def test_model_strcuture_category_unique_constraints(db_inspector):
    constraints = db_inspector.get_unique_constraints(TABLE_NAME)
    # print("Test Constraints...", constraints)

    assert any(
        constraint["name"] == "unq_category_name_level_constraint"
        for constraint in constraints
    )
    assert any(
        constraint["name"] == "unq_category_slug_constraint"
        for constraint in constraints
    )
