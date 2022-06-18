"""recreate file_maps table

Revision ID: 48db6963ab56
Revises: dcb059ce5b46
Create Date: 2022-06-18 21:54:35.776753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "48db6963ab56"
down_revision = "dcb059ce5b46"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table("file_maps")
    op.create_table(
        "file_maps",
        sa.Column("id", sa.Integer(), autoincrement=True, primary_key=True),
        sa.Column("createdTime", sa.Integer(), nullable=False),
        sa.Column("beforeType", sa.String(length=64), nullable=False),
        sa.Column("beforeHash", sa.String(length=256), nullable=False),
        sa.Column("afterType", sa.String(length=64), nullable=False),
        sa.Column("afterHash", sa.String(length=256), nullable=False),
        sa.Column("processType", sa.String(length=64), nullable=False),
    )


def downgrade():
    pass
