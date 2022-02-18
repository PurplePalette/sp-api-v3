"""add uploads table

Revision ID: ff159d52775e
Revises: 29b471b6dbb5
Create Date: 2022-02-18 23:43:41.040006

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ff159d52775e"
down_revision = "29b471b6dbb5"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "uploads",
        sa.Column("createdTime", sa.Integer(), nullable=True),
        sa.Column("updatedTime", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("userId", sa.Integer(), nullable=True),
        sa.Column("objectType", sa.String(length=64), nullable=True),
        sa.Column("objectSize", sa.Integer(), nullable=True),
        sa.Column("objectHash", sa.String(length=256), nullable=True),
        sa.Column("objectName", sa.String(length=256), nullable=True),
        sa.Column("objectTargetType", sa.String(length=32), nullable=True),
        sa.Column("objectTargetId", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["userId"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("uploads")
