import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = os.environ.get('SESSION_TYPE')
    TESTING = True
    DEBUG = True
    CORS_HEADERS = 'Content-Type'
    DATA_PER_PAGE = 7


class HomeBestConfig:
    load_dotenv()
    HOMEBEST_HOST = os.getenv('HOMEBEST_HOST')
    HOMEBEST_USER = os.getenv('HOMEBEST_USER')
    HOMEBEST_PASSWORD = os.getenv('HOMEBEST_PASSWORD')
    HOMEBEST_DATABASE = os.getenv('HOMEBEST_DATABASE')
    HOMEBEST_SERVER = os.getenv('HOMEBEST_SERVER')
