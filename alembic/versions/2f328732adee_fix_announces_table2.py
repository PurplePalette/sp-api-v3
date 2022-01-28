"""fix announces table2

Revision ID: 2f328732adee
Revises: 32ec65e865e4
Create Date: 2022-01-28 09:43:05.151505

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2f328732adee"
down_revision = "32ec65e865e4"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "announces",
        sa.Column("rating", sa.Integer(), nullable=True),
    )


def downgrade():
    op.drop_column("announces", "rating")
