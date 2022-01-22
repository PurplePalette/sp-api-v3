from os.path import dirname, join
import os

from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


USER = os.environ.get("DB_USER")
PASS = os.environ.get("DB_PASS")
HOST = os.environ.get("DB_HOST")
PORT = os.environ.get("PORT_DB")
DB = os.environ.get("DB_NAME")
ASYNC_DB_URL = f"mysql+aiomysql://{USER}:{PASS}@{HOST}/{DB}?charset=utf8"
DB_URL = f"mysql+pymysql://{USER}:{PASS}@{HOST}:{PORT}/{DB}?charset=utf8"
