TABLE_NAME = "product_line"


def test_model_structure_product_table_exists(db_inspector):
    assert db_inspector.has_table(TABLE_NAME)
