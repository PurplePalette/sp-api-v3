"""update levels table

Revision ID: 21e5008f643b
Revises: ff159d52775e
Create Date: 2022-02-19 01:57:07.065555

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "21e5008f643b"
down_revision = "ff159d52775e"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("levels", sa.Column("sus", sa.String(length=128), nullable=True))
    op.add_column(
        "levels",
        sa.Column("publicSus", sa.Boolean(), server_default="0", nullable=True),
    )


def downgrade():
    op.drop_column("levels", "publicSus")
    op.drop_column("levels", "sus")
