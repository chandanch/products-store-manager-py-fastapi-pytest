"""category_fields_default_value_added

Revision ID: 98ca051df4f0
Revises: 500dc30d659e
Create Date: 2024-08-23 19:25:36.635721

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "98ca051df4f0"
down_revision: Union[str, None] = "500dc30d659e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Manually adding the server_default changes
    op.alter_column("category", "is_active", server_default="False")
    op.alter_column("category", "level", server_default="100")


def downgrade():
    # Reverting the changes in the downgrade function
    op.alter_column("category", "is_active", server_default=None)
    op.alter_column("category", "level", server_default=None)
