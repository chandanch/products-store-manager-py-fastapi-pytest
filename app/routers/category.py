from typing import List
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


@category_router.get("/", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    try:
        categories = db.query(Category).all()
        return categories
    except Exception as e:
        print("Error when fetching category", e)
        raise HTTPException(status_code=500, detail="Internal server error")


# Endpoint to update an existing category
@category_router.put("/{category_id}", response_model=CategoryResponse, status_code=201)
def update_category(
    category_id: int,
    category_data: CategoryCreate,
    db: Session = Depends(get_db),
):
    try:
        category = db.query(Category).filter(Category.id == category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        for key, value in category_data.model_dump().items():
            setattr(category, key, value)
        db.commit()
        db.refresh(category)
        return category
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


# Endpoint to delete a category
@category_router.delete("/{category_id}", response_model=CategoryCreate)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    try:
        category = db.query(Category).filter(Category.id == category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        db.delete(category)
        db.commit()
        return category
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error while retrieving categories: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
