import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'
    DATA_PER_PAGE = 7


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

    
class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}


class HomeBestConfig:
    load_dotenv()
    HOMEBEST_HOST = os.getenv('HOMEBEST_HOST')
    HOMEBEST_USER = os.getenv('HOMEBEST_USER')
    HOMEBEST_PASSWORD = os.getenv('HOMEBEST_PASSWORD')
    HOMEBEST_DATABASE = os.getenv('HOMEBEST_DATABASE')
    HOMEBEST_SERVER = os.getenv('HOMEBEST_SERVER')
