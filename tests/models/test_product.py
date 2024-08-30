from sqlalchemy import Integer, String, Boolean


TABLE_NAME = "product"


def test_model_structure_product_table_exists(db_inspector):
    assert db_inspector.has_table(TABLE_NAME)


def test_model_structure_product_column_types(db_inspector):
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
