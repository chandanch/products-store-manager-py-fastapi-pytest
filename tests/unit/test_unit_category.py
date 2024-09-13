import pytest
from app.schemas.category_schema import CategoryCreate
from app.models import Category
from pydantic import ValidationError
from fastapi import HTTPException


from factories.models_factory import generate_random_category_as_dict


def mock_output(return_value=None):
    """
    Returns a lamba function and echoes args and kwargs
    """
    return lambda *args, **kwargs: return_value


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


def test_unit_create_category_success(client, monkeypatch):

    mock_category_data = generate_random_category_as_dict()

    for key, value in mock_category_data.items():
        monkeypatch.setattr(Category, key, value)

    monkeypatch.setattr("sqlalchemy.orm.Query.first", mock_output())
    monkeypatch.setattr("sqlalchemy.orm.Session.commit", mock_output())
    monkeypatch.setattr("sqlalchemy.orm.Session.refresh", mock_output())

    clone_mock_category_data = mock_category_data.copy()

    clone_mock_category_data.pop("id")
    response = client.post("api/category", json=clone_mock_category_data)
    assert response.status_code == 201
    assert response.json() == mock_category_data


@pytest.mark.parametrize(
    "existing_category, category_data, expected_detail",
    [
        (
            True,
            generate_random_category_as_dict(),
            "Category name and level already exists",
        ),
        (True, generate_random_category_as_dict(), "Category slug already exists"),
    ],
)
def test_unit_create_new_category_existing(
    client, monkeypatch, existing_category, category_data, expected_detail
):
    def mock_check_existing_category(db, category_data):
        if existing_category:
            raise HTTPException(status_code=400, detail=expected_detail)

    monkeypatch.setattr(
        "app.routers.category_routes.check_existing_category",
        mock_check_existing_category,
    )

    monkeypatch.setattr("sqlalchemy.orm.Query.first", mock_output())
    body = category_data.copy()
    body.pop("id")
    response = client.post("api/category/", json=body)

    assert response.status_code == 400

    if expected_detail:
        assert response.json() == {"detail": expected_detail}


def test_unit_create_new_category_with_internal_server_error(client, monkeypatch):
    category = generate_random_category_as_dict()

    # Mock an exception to simulate an internal server error
    def mock_create_category_exception(*args, **kwargs):
        raise Exception("Internal server error")

    for key, value in category.items():
        monkeypatch.setattr(Category, key, value)
    monkeypatch.setattr("sqlalchemy.orm.Query.first", mock_output())
    monkeypatch.setattr("sqlalchemy.orm.Session.commit", mock_create_category_exception)

    body = category.copy()
    body.pop("id")
    response = client.post("/api/category/", json=body)
    assert response.status_code == 500
