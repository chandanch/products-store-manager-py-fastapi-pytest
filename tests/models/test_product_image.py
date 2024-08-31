from sqlalchemy import Integer, String

TABLE_NAME = "product_image"


def test_model_structure_product_image_table_exists(db_inspector):
    assert db_inspector.has_table(TABLE_NAME)


def test_model_structure_product_image_column_types(db_inspector):
    columns = {
        columns["name"]: columns for columns in db_inspector.get_columns(TABLE_NAME)
    }

    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["alternative_text"]["type"], String)
    assert isinstance(columns["url"]["type"], String)
    assert isinstance(columns["order"]["type"], Integer)
    assert isinstance(columns["product_line_id"]["type"], Integer)


def test_model_structure_product_image_nullable_constraints(db_inspector):
    columns = db_inspector.get_columns(TABLE_NAME)

    expected_nullable_columns = {
        "id": False,
        "alternative_text": False,
        "url": False,
        "order": False,
        "product_line_id": False,
    }

    for column in columns:
        # print(f"Column: {column}")
        # Raise assertion error with an optional error message
        assert column["nullable"] == expected_nullable_columns.get(
            column["name"]
        ), f"Column '{column['name']}' cannot be null"


def test_model_structure_product_image_column_constraints(db_inspector):
    constraints = db_inspector.get_check_constraints(TABLE_NAME)

    assert any(
        constraint["name"] == "product_image_alternative_text_constraint"
        for constraint in constraints
    )

    assert any(
        constraint["name"] == "product_image_url_constraint"
        for constraint in constraints
    )

    assert any(
        constraint["name"] == "product_line_order_range_constraint"
        for constraint in constraints
    )


def test_model_structure_product_image_unique_constraints(db_inspector):
    constraints = db_inspector.get_unique_constraints(TABLE_NAME)
    # print("Test Constraints...", constraints)

    assert any(
        constraint["name"] == "unq_product_image_order_product_line_id_constraint"
        for constraint in constraints
    )


def test_model_structure_product_line_foreign_key(db_inspector):
    foreign_keys = db_inspector.get_foreign_keys(TABLE_NAME)
    product_id_fkey = next(
        (
            fk
            for fk in foreign_keys
            if set(fk["constrained_columns"]) == {"product_line_id"}
        ),
        None,
    )

    assert product_id_fkey is not None
