"""update announces table

Revision ID: 82b7b47c06f3
Revises: 886ce6d09526
Create Date: 2022-01-28 09:16:33.310515

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "82b7b47c06f3"
down_revision = "886ce6d09526"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("announces", "artists")
    op.drop_column("announces", "artistsEn")
    op.add_column(
        "announces",
        sa.Column("subtitle", sa.String(length=128), nullable=True),
    )
    op.add_column(
        "announces",
        sa.Column("subtitleEn", sa.String(length=128), nullable=True),
    )


def downgrade():
    op.add_column(
        "announces",
        sa.Column("artists", sa.String(length=128), nullable=True),
    )
    op.add_column(
        "announces",
        sa.Column("artistsEn", sa.String(length=128), nullable=True),
    )
