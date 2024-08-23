from sqlalchemy import Column, Integer, String, Boolean

from app.settings.db_connection import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    slug = Column(String(120))
    is_active = Column(Boolean)
    level = Column(Integer)
    parent_id = Column(Integer)
