"""change field xyzHash to xyz

Revision ID: 29b471b6dbb5
Revises: cc0b30214314
Create Date: 2022-01-30 11:23:15.292914

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "29b471b6dbb5"
down_revision = "cc0b30214314"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "backgrounds", sa.Column("thumbnail", sa.String(length=128), nullable=True)
    )
    op.add_column(
        "backgrounds", sa.Column("data", sa.String(length=128), nullable=True)
    )
    op.add_column(
        "backgrounds", sa.Column("image", sa.String(length=128), nullable=True)
    )
    op.add_column(
        "backgrounds", sa.Column("configuration", sa.String(length=128), nullable=True)
    )
    op.drop_column("backgrounds", "thumbnailHash")
    op.drop_column("backgrounds", "imageHash")
    op.drop_column("backgrounds", "dataHash")
    op.add_column(
        "effects", sa.Column("thumbnail", sa.String(length=128), nullable=True)
    )
    op.add_column("effects", sa.Column("data", sa.String(length=128), nullable=True))
    op.drop_column("effects", "thumbnailHash")
    op.drop_column("effects", "dataHash")
    op.add_column(
        "engines", sa.Column("thumbnail", sa.String(length=128), nullable=True)
    )
    op.add_column("engines", sa.Column("data", sa.String(length=128), nullable=True))
    op.add_column(
        "engines", sa.Column("configuration", sa.String(length=128), nullable=True)
    )
    op.drop_column("engines", "thumbnailHash")
    op.drop_column("engines", "configurationHash")
    op.drop_column("engines", "dataHash")
    op.add_column("levels", sa.Column("cover", sa.String(length=128), nullable=True))
    op.add_column("levels", sa.Column("bgm", sa.String(length=128), nullable=True))
    op.add_column("levels", sa.Column("data", sa.String(length=128), nullable=True))
    op.drop_column("levels", "bgmHash")
    op.drop_column("levels", "dataHash")
    op.drop_column("levels", "coverHash")
    op.add_column(
        "particles", sa.Column("thumbnail", sa.String(length=128), nullable=True)
    )
    op.add_column("particles", sa.Column("data", sa.String(length=128), nullable=True))
    op.add_column(
        "particles", sa.Column("texture", sa.String(length=128), nullable=True)
    )
    op.drop_column("particles", "textureHash")
    op.drop_column("particles", "thumbnailHash")
    op.drop_column("particles", "dataHash")
    op.add_column("skins", sa.Column("thumbnail", sa.String(length=128), nullable=True))
    op.add_column("skins", sa.Column("data", sa.String(length=128), nullable=True))
    op.add_column("skins", sa.Column("texture", sa.String(length=128), nullable=True))
    op.drop_column("skins", "textureHash")
    op.drop_column("skins", "thumbnailHash")
    op.drop_column("skins", "dataHash")


def downgrade():
    op.add_column(
        "skins", sa.Column("dataHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.add_column(
        "skins", sa.Column("thumbnailHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.add_column(
        "skins", sa.Column("textureHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.drop_column("skins", "texture")
    op.drop_column("skins", "data")
    op.drop_column("skins", "thumbnail")
    op.add_column(
        "particles", sa.Column("dataHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.add_column(
        "particles",
        sa.Column("thumbnailHash", mysql.VARCHAR(length=128), nullable=True),
    )
    op.add_column(
        "particles", sa.Column("textureHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.drop_column("particles", "texture")
    op.drop_column("particles", "data")
    op.drop_column("particles", "thumbnail")
    op.add_column(
        "levels", sa.Column("coverHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.add_column(
        "levels", sa.Column("dataHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.add_column(
        "levels", sa.Column("bgmHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.drop_column("levels", "data")
    op.drop_column("levels", "bgm")
    op.drop_column("levels", "cover")
    op.add_column(
        "engines", sa.Column("dataHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.add_column(
        "engines",
        sa.Column("configurationHash", mysql.VARCHAR(length=128), nullable=True),
    )
    op.add_column(
        "engines", sa.Column("thumbnailHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.drop_column("engines", "configuration")
    op.drop_column("engines", "data")
    op.drop_column("engines", "thumbnail")
    op.add_column(
        "effects", sa.Column("dataHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.add_column(
        "effects", sa.Column("thumbnailHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.drop_column("effects", "data")
    op.drop_column("effects", "thumbnail")
    op.add_column(
        "backgrounds", sa.Column("dataHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.add_column(
        "backgrounds", sa.Column("imageHash", mysql.VARCHAR(length=128), nullable=True)
    )
    op.add_column(
        "backgrounds",
        sa.Column("thumbnailHash", mysql.VARCHAR(length=128), nullable=True),
    )
    op.drop_column("backgrounds", "configuration")
    op.drop_column("backgrounds", "image")
    op.drop_column("backgrounds", "data")
    op.drop_column("backgrounds", "thumbnail")
