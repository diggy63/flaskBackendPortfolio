import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.getenv("DB_HOST")
SQLALCHEMY_TRACK_MODIFICATIONS = False