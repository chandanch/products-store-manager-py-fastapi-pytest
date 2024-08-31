from sqlalchemy import Integer, String, DateTime

TABLE_NAME = "seasonal_event"


def test_model_structure_seasonal_event_table_exists(db_inspector):
    assert db_inspector.has_table(TABLE_NAME)


def test_model_structure_seasonal_event_column_types(db_inspector):
    columns = {
        columns["name"]: columns for columns in db_inspector.get_columns(TABLE_NAME)
    }

    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["start_date"]["type"], DateTime)
    assert isinstance(columns["end_date"]["type"], DateTime)
    assert isinstance(columns["name"]["type"], String)


def test_model_structure_seasonal_event_nullable_constraints(db_inspector):
    columns = db_inspector.get_columns(TABLE_NAME)

    expected_nullable_columns = {
        "id": False,
        "start_date": False,
        "end_date": False,
        "name": False,
    }

    for column in columns:
        # print(f"Column: {column}")
        # Raise assertion error with an optional error message
        assert column["nullable"] == expected_nullable_columns.get(
            column["name"]
        ), f"Column '{column['name']}' cannot be null"


def test_model_structure_seasonal_event_column_constraints(db_inspector):
    constraints = db_inspector.get_check_constraints(TABLE_NAME)

    assert any(
        constraint["name"] == "seasonal_event_name_length_constraint"
        for constraint in constraints
    )


def test_model_structure_seasonal_event_unique_constraints(db_inspector):
    constraints = db_inspector.get_unique_constraints(TABLE_NAME)
    # print("Test Constraints...", constraints)

    assert any(
        constraint["name"] == "unq_seasonal_event_name_constraint"
        for constraint in constraints
    )
