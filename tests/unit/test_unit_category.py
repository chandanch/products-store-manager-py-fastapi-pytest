# import pytest
# from app.schemas.category_schema import CategoryCreate
from app.models import Category

# from pydantic import ValidationError
# from app.routers import category

# from fastapi import HTTPException


from factories.models_factory import generate_random_category_as_dict


def mock_output(return_value=None):
    """
    Returns a lamba function and echoes args and kwargs
    """
    # print("Mock Function called =====")
    return lambda *args, **kwargs: return_value


def test_unit_create_category_success(client, monkeypatch):

    mock_category_data = generate_random_category_as_dict()

    for key, value in mock_category_data.items():
        monkeypatch.setattr(Category, key, value)

    def mock_check_existing_category(db, category_data):
        return True

    monkeypatch.setattr("sqlalchemy.orm.Query.first", mock_output())
    monkeypatch.setattr("sqlalchemy.orm.Session.commit", mock_output())
    monkeypatch.setattr("sqlalchemy.orm.Session.refresh", mock_output())
    # monkeypatch.setattr(category, "auth_requests", mock_output())
    # monkeypatch.setattr("app.routers.category.get_db", mock_output())
    monkeypatch.setattr(
        "app.routers.category.check_existing_category",
        mock_check_existing_category,
    )

    clone_mock_category_data = mock_category_data.copy()

    clone_mock_category_data.pop("id")
    response = client.post("api/category/", json=clone_mock_category_data)
    assert response.status_code == 201
    assert response.json() == mock_category_data
