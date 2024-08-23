"""category_fields_nullable_constraints

Revision ID: 500dc30d659e
Revises: 9b7e42f7d428
Create Date: 2024-08-23 18:05:24.816354

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '500dc30d659e'
down_revision: Union[str, None] = '9b7e42f7d428'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('category', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('category', 'slug',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('category', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('category', 'level',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('category', 'level',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('category', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('category', 'slug',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('category', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###