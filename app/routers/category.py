from fastapi import APIRouter, Depends
from app.models import Category
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

from app.schemas.category_schema import CategoryResponse, CategoryCreate
from app.settings.db_connection import get_db
from app.utils.category_utils import check_existing_category


category_router = APIRouter()


@category_router.post("/", response_model=CategoryResponse, status_code=201)
def add_category(category_data: CategoryCreate, db: Session = Depends(get_db)):
    try:
        check_existing_category(db, category_data)
        new_category = Category(**category_data.model_dump())

        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")
