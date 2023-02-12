import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:@localhost/reservations"
SQLALCHEMY_TRACK_MODIFICATIONS = False