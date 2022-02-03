import os
from os.path import dirname, join

from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


CDN_ENDPOINT = os.environ.get("CDN_ENDPOINT")

SONOLUS_VERSION = "0.5.10"
BACKGROUND_VERSION = 1
