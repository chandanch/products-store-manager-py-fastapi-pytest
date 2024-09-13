from fastapi import APIRouter, Depends, Request
from app.models import Category
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

from app.schemas.category_schema import CategoryResponse, CategoryCreate
from app.settings.db_connection import get_db
from app.utils.category_utils import check_existing_category
from app.middlewares.auth_middleware import auth_requests

category_router = APIRouter()


@category_router.post("/", response_model=CategoryResponse, status_code=201)
@auth_requests
def add_category(
    request: Request, category_data: CategoryCreate, db: Session = Depends(get_db)
):
    try:
        check_existing_category(db, category_data)
        new_category = Category(**category_data.model_dump())

        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        print("Error when creating category", e)
        raise HTTPException(status_code=500, detail="Internal server error")
