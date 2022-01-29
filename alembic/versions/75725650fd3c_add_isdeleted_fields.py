"""add isDeleted fields

Revision ID: 75725650fd3c
Revises: 43742645c77a
Create Date: 2022-01-30 05:49:56.963122

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "75725650fd3c"
down_revision = "43742645c77a"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "backgrounds",
        sa.Column("isDeleted", sa.Boolean(), server_default="0", nullable=True),
    )
    op.add_column(
        "effects",
        sa.Column("isDeleted", sa.Boolean(), server_default="0", nullable=True),
    )
    op.add_column(
        "engines",
        sa.Column("isDeleted", sa.Boolean(), server_default="0", nullable=True),
    )
    op.add_column(
        "levels",
        sa.Column("isDeleted", sa.Boolean(), server_default="0", nullable=True),
    )
    op.add_column(
        "particles",
        sa.Column("isDeleted", sa.Boolean(), server_default="0", nullable=True),
    )
    op.add_column(
        "skins", sa.Column("isDeleted", sa.Boolean(), server_default="0", nullable=True)
    )


def downgrade():
    op.drop_column("skins", "isDeleted")
    op.drop_column("particles", "isDeleted")
    op.drop_column("levels", "isDeleted")
    op.drop_column("engines", "isDeleted")
    op.drop_column("effects", "isDeleted")
    op.drop_column("backgrounds", "isDeleted")
