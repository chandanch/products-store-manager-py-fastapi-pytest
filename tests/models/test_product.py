TABLE_NAME = "product"


def test_model_structure_category_table_exists(db_inspector):
    assert db_inspector.has_table(TABLE_NAME)
