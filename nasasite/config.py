import os
import dotenv

dotenv.load_dotenv("../.env")


class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    DB_HOST = os.environ["DB_HOST"]
    DB_PORT = os.environ["DB_PORT"]
    DB_NAME = os.environ["DB_NAME"]
    DB_USER = os.environ["DB_USER"]
    DB_PASS = os.environ["DB_PASS"]
    DEBUG = os.environ.get("DEBUG") == "1"
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(", ")
