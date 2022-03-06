import os
from os.path import dirname, join

from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

USER = os.environ.get("DB_USER")
PASS = os.environ.get("DB_PASS")
HOST = os.environ.get("DB_HOST")
PORT = os.environ.get("PORT_DB")
DB = os.environ.get("DB_NAME")
ASYNC_DB_URL = f"mysql+aiomysql://{USER}:{PASS}@{HOST}:{PORT}/{DB}?charset=utf8"
DB_URL = f"mysql+pymysql://{USER}:{PASS}@{HOST}:{PORT}/{DB}?charset=utf8"

CDN_ENDPOINT = os.environ.get("CDN_ENDPOINT")
S3_ENDPOINT = os.environ.get("S3_ENDPOINT")
S3_BUCKET = os.environ.get("S3_BUCKET")
S3_KEY = os.environ.get("S3_KEY")
S3_SECRET = os.environ.get("S3_SECRET")


# Server support version
SKIN_VERSION = 2
ENGINE_VERSION = 4
BACKGROUND_VERSION = 2
EFFECT_VERSION = 2
LEVEL_VERSION = 1
PARTICLE_VERSION = 1
SONOLUS_VERSION = "0.5.10"
