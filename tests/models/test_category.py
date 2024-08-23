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

    print(columns)
