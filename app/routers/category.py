from fastapi import APIRouter, Depends
from app.models import Category
from sqlalchemy.orm import Session

from app.schemas.category_schema import CategoryResponse, CategoryCreate
from app.settings.db_connection import get_db


category_router = APIRouter()
# db = SessionLocal()


@category_router.post("/", response_model=CategoryResponse, status_code=201)
def add_category(category_data: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(**category_data.model_dump())

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category
