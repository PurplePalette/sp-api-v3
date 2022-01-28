"""fix announces table

Revision ID: 32ec65e865e4
Revises: 82b7b47c06f3
Create Date: 2022-01-28 09:39:49.205107

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "32ec65e865e4"
down_revision = "82b7b47c06f3"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("announces", "coverHash")
    op.drop_column("announces", "bgmHash")
    op.drop_column("announces", "dataHash")
    op.add_column(
        "announces",
        sa.Column("cover", sa.String(length=128), nullable=True),
    )
    op.add_column(
        "announces",
        sa.Column("preview", sa.String(length=128), nullable=True),
    )
    op.add_column(
        "announces",
        sa.Column("bgm", sa.String(length=128), nullable=True),
    )


def downgrade():
    op.add_column(
        "announces",
        sa.Column("coverHash", sa.String(length=128), nullable=True),
    )
    op.add_column(
        "announces",
        sa.Column("bgmHash", sa.String(length=128), nullable=True),
    )
    op.add_column(
        "announces",
        sa.Column("dataHash", sa.String(length=128), nullable=True),
    )
