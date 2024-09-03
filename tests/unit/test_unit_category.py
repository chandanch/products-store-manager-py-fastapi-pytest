import pytest
from app.schemas.category_schema import CategoryCreate
from pydantic import ValidationError


def test_unit_schema_category_validation():
    valid_data = {
        "name": "test category",
        "slug": "test-slug",
    }
    category = CategoryCreate(**valid_data)
    assert category.name == "test category"
    assert category.is_active is False
    assert category.level == 100
    assert category.parent_id is None

    invalid_data = {
        "name": "test category",
    }
    with pytest.raises(ValidationError):
        CategoryCreate(**invalid_data)
