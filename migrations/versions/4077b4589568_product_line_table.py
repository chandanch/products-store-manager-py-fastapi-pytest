"""product_line_table

Revision ID: 4077b4589568
Revises: af323ca2bca2
Create Date: 2024-08-31 13:14:54.544696

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4077b4589568"
down_revision: Union[str, None] = "af323ca2bca2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "product_line",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("price", sa.DECIMAL(precision=5, scale=2), nullable=True),
        sa.Column(
            "sku",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("stock_qty", sa.Integer(), server_default="0", nullable=False),
        sa.Column("is_active", sa.Boolean(), server_default="false", nullable=False),
        sa.Column("order", sa.Integer(), nullable=False),
        sa.Column("weight", sa.Float(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_unique_constraint(
        "unq_product_line_sku_constraint", "product_line", ["sku"]
    )
    op.create_unique_constraint(
        "unq_product_line_order_product_id_constraint",
        "product_line",
        ["order", "product_id"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("unq_category_name_level_constraint", "category", type_="unique")
    op.drop_constraint("unq_category_slug_constraint", "category", type_="unique")
    op.drop_constraint("unq_product_name_constraint", "product", type_="unique")
    op.drop_constraint("unq_product_slug_constraint", "product", type_="unique")
    op.drop_table("product_line")
    # ### end Alembic commands ###