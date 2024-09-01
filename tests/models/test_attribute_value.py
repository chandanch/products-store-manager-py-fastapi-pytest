from sqlalchemy import Integer, String

"""
## Table and Column Validation
"""

"""
- [ ] Confirm the presence of all required tables within the database schema.
"""


def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("attribute_value")


"""
- [ ] Validate the existence of expected columns in each table, ensuring correct data types.
"""


def test_model_structure_column_data_types(db_inspector):
    table = "attribute_value"
    columns = {columns["name"]: columns for columns in db_inspector.get_columns(table)}

    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["attribute_value"]["type"], String)
    assert isinstance(columns["attribute_id"]["type"], Integer)


"""
- [ ] Ensure that column foreign keys correctly defined.
"""


def test_model_structure_foreign_key(db_inspector):
    table = "attribute_value"
    foreign_keys = db_inspector.get_foreign_keys(table)
    attribute_value_foreign_key = next(
        (
            fk
            for fk in foreign_keys
            if set(fk["constrained_columns"]) == {"attribute_id"}
        ),
        None,
    )
    assert attribute_value_foreign_key is not None


"""
- [ ] Verify nullable or not nullable fields
"""


def test_model_structure_nullable_constraints(db_inspector):
    table = "attribute_value"
    columns = db_inspector.get_columns(table)

    expected_nullable = {
        "id": False,
        "attribute_value": False,
        "attribute_id": False,
    }

    for column in columns:
        column_name = column["name"]
        assert column["nullable"] == expected_nullable.get(
            column_name
        ), f"column '{column_name}' is not nullable as expected"


"""
- [ ] Test columns with specific constraints to ensure they are accurately defined.
"""


def test_model_structure_column_constraints(db_inspector):
    table = "attribute_value"
    constraints = db_inspector.get_check_constraints(table)

    assert any(
        constraint["name"] == "attribute_value_name_length_check"
        for constraint in constraints
    )


"""
- [ ] Verify the correctness of default values for relevant columns.
"""


"""
- [ ] Ensure that column lengths align with defined requirements.
"""


def test_model_structure_column_lengths(db_inspector):
    table = "attribute_value"
    columns = {columns["name"]: columns for columns in db_inspector.get_columns(table)}

    assert columns["attribute_value"]["type"].length == 100


"""
- [ ]  Validate the enforcement of unique constraints for columns requiring unique values.
"""


def test_model_structure_unique_constraints(db_inspector):
    table = "attribute_value"
    constraints = db_inspector.get_unique_constraints(table)

    assert any(
        constraint["name"] == "uq_attribute_value_attribute_id"
        for constraint in constraints
    )
