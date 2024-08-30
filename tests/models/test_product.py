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

    # print(columns)
