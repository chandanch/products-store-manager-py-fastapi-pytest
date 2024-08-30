from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    CheckConstraint,
    UniqueConstraint,
    Text,
    DateTime,
    text,
    func,
    Enum,
    ForeignKey,
)

from app.settings.db_connection import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(String(140), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False, server_default="False")
    level = Column(Integer, nullable=False, default="100", server_default="100")
    parent_id = Column(Integer, ForeignKey("category.id"), nullable=True)

    __tableargs__ = (
        CheckConstraint("LENGTH(name) > 0", name="name_length_constraint"),
        CheckConstraint("LENGTH(slug) > 0", name="slugh_length_constraint"),
        UniqueConstraint("name", "level", name="unq_category_name_level_constraint"),
        UniqueConstraint("slug", name="unq_category_slug_constraint"),
    )


class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    slug = Column(String(220), nullable=False)
    description = Column(Text, nullable=True)
    is_digital = Column(Boolean, nullable=False, default=False, server_default="False")
    created_at = Column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=func.now(),
    )
    is_active = Column(Boolean, nullable=False, default=False, server_default="False")
    stock_status = Column(
        Enum(
            "outofstock",
            "available",
            "ordered",
            name="status_enum",
        ),
        nullable=False,
        server_default="outofstock",
    )
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    seasonal_event = Column(Integer, ForeignKey("seasonal_event.id"), nullable=False)
