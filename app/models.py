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
    DECIMAL,
    Float,
)
from sqlalchemy.dialects.postgresql import UUID

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

    __table_args__ = (
        CheckConstraint("LENGTH(name) > 0", name="name_length_constraint"),
        CheckConstraint("LENGTH(slug) > 0", name="slugh_length_constraint"),
        UniqueConstraint("name", "level", name="unq_category_name_level_constraint"),
        UniqueConstraint("slug", name="unq_category_slug_constraint"),
    )


class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key=True, nullable=False)
    pid = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        server_default=text("uuid_generate_v4()"),
    )
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
    seasonal_event = Column(Integer, ForeignKey("seasonal_event.id"), nullable=True)

    __table_args__ = (
        CheckConstraint("LENGTH(name) > 0", name="product_name_length_constraint"),
        CheckConstraint("LENGTH(slug) > 0", name="product_slug_length_constraint"),
        UniqueConstraint("name", name="unq_product_name_constraint"),
        UniqueConstraint("slug", name="unq_product_slug_constraint"),
    )


class ProductLine(Base):

    __tablename__ = "product_line"

    id = Column(Integer, primary_key=True, nullable=False)
    price = Column(DECIMAL(precision=5, scale=2), nullable=False)
    sku = Column(
        UUID(as_uuid=True),
        nullable=False,
        server_default=text("uuid_generate_v4()"),
    )
    stock_qty = Column(Integer, nullable=False, default=0, server_default="0")
    is_active = Column(Boolean, nullable=False, default=False, server_default="false")
    order = Column("order", Integer, nullable=False, quote=True)
    weight = Column(Float, nullable=False)
    created_at = Column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "price >=0 AND price <=999.99", name="product_line_price_max_constraint"
        ),
        CheckConstraint(
            '"order" >= 1 AND "order" <=20', name="product_line_order_range_constraint"
        ),
        UniqueConstraint(
            "order", "product_id", name="unq_product_line_order_product_id_constraint"
        ),
        UniqueConstraint("sku", name="unq_product_line_sku_constraint"),
    )


class ProductImage(Base):
    __tablename__ = "product_image"

    id = Column(Integer, primary_key=True, nullable=False)
    alternative_text = Column(String(100), nullable=False)
    url = Column(String(200), nullable=False)
    order = Column("order", Integer, nullable=False)
    product_line_id = Column(Integer, ForeignKey("product_line.id"), nullable=False)

    __table_args__ = (
        CheckConstraint(
            '"order" >= 1 AND "order" <=20', name="product_line_order_range_constraint"
        ),
        CheckConstraint("LENGTH(url) > 0", name="product_image_url_constraint"),
        CheckConstraint(
            "LENGTH(alternative_text) > 0",
            name="product_image_alternative_text_constraint",
        ),
        UniqueConstraint(
            "order",
            "product_line_id",
            name="unq_product_image_order_product_line_id_constraint",
        ),
    )


class SeasonalEvent(Base):
    __tablename__ = "seasonal_event"

    id = Column(Integer, primary_key=True, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    name = Column(String(100), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "LENGTH(name) > 0", name="seasonal_event_name_length_constraint"
        ),
        UniqueConstraint(
            "name",
            name="unq_seasonal_event_name_constraint",
        ),
    )


class Attribute(Base):
    __tablename__ = "attribute"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=True)

    __table_args__ = (
        CheckConstraint(
            "LENGTH(name) > 0",
            name="attribute_name_length_check",
        ),
        UniqueConstraint("name", name="uq_attribute_name"),
    )


class ProductType(Base):
    __tablename__ = "product_type"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    level = Column(
        Integer,
        nullable=False,
    )
    parent_id = Column(Integer, ForeignKey("product_type.id"), nullable=True)

    __table_args__ = (
        CheckConstraint("LENGTH(name) > 0", name="product_type_name_length_check"),
        UniqueConstraint("name", "level", name="uq_product_type_name_level"),
    )


class AttributeValue(Base):
    __tablename__ = "attribute_value"

    id = Column(Integer, primary_key=True, nullable=False)
    attribute_value = Column(String(100), nullable=False)
    attribute_id = Column(Integer, ForeignKey("attribute.id"), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "LENGTH(attribute_value) > 0", name="attribute_value_name_length_check"
        ),
        UniqueConstraint(
            "attribute_value", "attribute_id", name="uq_attribute_value_attribute_id"
        ),
    )
