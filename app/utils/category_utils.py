from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Category
from app.schemas.category_schema import CategoryCreate


def check_existing_category(db: Session, category_data: CategoryCreate):
    existing_category = (
        db.query(Category)
        .filter(
            (Category.slug == category_data.slug)
            | (Category.name == category_data.name)
            & (Category.level == category_data.level)
        )
        .first()
    )

    if existing_category:
        if (
            existing_category.name == category_data.name
            and existing_category.level == category_data.level
        ):
            detail_msg = "Category name and level already exists"
        else:
            detail_msg = "Category slug already exists"

        raise HTTPException(status_code=400, detail=detail_msg)
