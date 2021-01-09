import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

def _get_database(server):
    load_dotenv()

    host = os.environ.get('DATABASE_HOST')
    user = os.environ.get('DATABASE_USER')
    password = os.environ.get('DATABASE_PASSWORD')
    database = os.environ.get('DATABASE_NAME')
    if server == 'pythonanywhere':
        return "mysql://{}:{}@{}/{}".format(user,password,host,database)
    else:
        return "mysql+pymysql://{}:{}@{}/{}".format(user,password,host,database)


class Config(object):
    load_dotenv()

    SECRET_KEY = os.environ.get('SECRET_KEY')

    """ FLASK-CORS """
    CORS_HEADERS = 'Content-Type'

    """ PAGINATION """
    DATA_PER_PAGE = 7

    # Add your configurations here


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_DATABASE_URI = _get_database('localhost')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    # SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """
    SQLALCHEMY_DATABASE_URI = _get_database('pythonanywhere')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True
    # SQLALCHEMY_ECHO = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}


class HomeBestConfig:
    load_dotenv()
    HOST = os.environ.get('DATABASE_HOST')
    USER = os.environ.get('DATABASE_USER')
    PASSWORD = os.environ.get('DATABASE_PASSWORD')
    DATABASE = os.environ.get('DATABASE_NAME')
