from sqlalchemy import Integer, Boolean, Numeric, Float
from sqlalchemy.dialects.postgresql import UUID


TABLE_NAME = "product_line"


def test_model_structure_product_line_table_exists(db_inspector):
    assert db_inspector.has_table(TABLE_NAME)


def test_model_structure_product_line_column_types(db_inspector):
    columns = {
        columns["name"]: columns for columns in db_inspector.get_columns(TABLE_NAME)
    }

    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["price"]["type"], type(Numeric(precision=5, scale=2)))
    assert isinstance(columns["sku"]["type"], UUID)
    assert isinstance(columns["stock_qty"]["type"], Integer)
    assert isinstance(columns["is_active"]["type"], Boolean)
    assert isinstance(columns["order"]["type"], Integer)
    assert isinstance(columns["weight"]["type"], Float)
    assert isinstance(columns["product_id"]["type"], Integer)


def test_model_structure_product_line_nullable_constraints(db_inspector):
    columns = db_inspector.get_columns(TABLE_NAME)

    expected_nullable_columns = {
        "id": False,
        "price": False,
        "sku": False,
        "stock_qty": False,
        "is_active": False,
        "order": False,
        "weight": False,
        "product_id": False,
        "created_at": False,
    }

    for column in columns:
        # print(f"Column: {column}")
        # Raise assertion error with an optional error message
        assert column["nullable"] == expected_nullable_columns.get(
            column["name"]
        ), f"Column '{column['name']}' cannot be null"


def test_model_structure_product_line_column_constraints(db_inspector):
    constraints = db_inspector.get_check_constraints(TABLE_NAME)

    assert any(
        constraint["name"] == "product_line_order_range_constraint"
        for constraint in constraints
    )

    assert any(
        constraint["name"] == "product_line_price_max_constraint"
        for constraint in constraints
    )


def test_model_structure_product_line_default_values(db_inspector):
    columns = {
        columns["name"]: columns for columns in db_inspector.get_columns(TABLE_NAME)
    }
    # print(columns)
    assert columns["stock_qty"]["default"] == "0"
    assert columns["is_active"]["default"] == "false"


def test_model_structure_product_line_unique_constraints(db_inspector):
    constraints = db_inspector.get_unique_constraints(TABLE_NAME)
    # print("Test Constraints...", constraints)

    assert any(
        constraint["name"] == "unq_product_line_sku_constraint"
        for constraint in constraints
    )
    assert any(
        constraint["name"] == "unq_product_line_order_product_id_constraint"
        for constraint in constraints
    )


def test_model_structure_product_line_foreign_key(db_inspector):
    foreign_keys = db_inspector.get_foreign_keys(TABLE_NAME)
    product_id_fkey = next(
        (fk for fk in foreign_keys if set(fk["constrained_columns"]) == {"product_id"}),
        None,
    )

    assert product_id_fkey is not None
