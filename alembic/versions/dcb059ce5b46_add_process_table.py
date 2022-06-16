"""add_process_table

Revision ID: dcb059ce5b46
Revises: 21e5008f643b
Create Date: 2022-06-12 19:09:48.636469

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "dcb059ce5b46"
down_revision = "21e5008f643b"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "file_maps",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("createdTime", sa.Integer(), nullable=False),
        sa.Column("beforeType", sa.String(length=64), nullable=False),
        sa.Column("beforeHash", sa.String(length=256), nullable=False),
        sa.Column("afterType", sa.String(length=64), nullable=False),
        sa.Column("afterHash", sa.String(length=256), nullable=False),
        sa.Column("processType", sa.String(length=64), nullable=False),
    )


def downgrade():
    op.drop_table("file_maps")
