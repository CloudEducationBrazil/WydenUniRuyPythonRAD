import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
