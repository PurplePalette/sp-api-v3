"""fix users table

Revision ID: 43742645c77a
Revises: 2f328732adee
Create Date: 2022-01-28 11:33:43.002992

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "43742645c77a"
down_revision = "2f328732adee"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "users",
        sa.Column(
            "description", sa.String(length=512), server_default="", nullable=True
        ),
    )


def downgrade():
    op.drop_column("users", "description")
