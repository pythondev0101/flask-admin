import os
from dotenv import load_dotenv



basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    load_dotenv()

    SECRET_KEY = os.environ.get('SECRET_KEY') # Key

    CORS_HEADERS = 'Content-Type' # Flask Cors

    # DEVELOPERS-NOTE: ADMIN PAGE CONFIGURATIONS HERE
    ADMIN = {
        'APPLICATION_NAME': 'Likes',
        'DATA_PER_PAGE': 25,
        'HOME_URL': 'bp_admin.dashboard',
        'DASHBOARD_URL': 'bp_admin.dashboard',
        'MODELS_SIDEBAR_HEADER': 'SYSTEM MODELS'
    }
    #                 -END-

    # DEVELOPERS-NOTE: AUTH CONFIGURATIONS HERE
    AUTH = {
        'LOGIN_REDIRECT_URL': 'bp_admin.dashboard',
    }
    #                 -END-

    # DEVELOPERS-NOTE: -ADD YOUR CONFIGURATIONS HERE-
    
    #                 -END-


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    load_dotenv()
    
    MONGO_URI = os.environ.get('MONGO_URI_DEV')
    MONGODB_HOST = os.environ.get('MONGO_URI_DEV')
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    load_dotenv()
    
    MONGO_URI = os.environ.get('MONGO_URI_PROD')
    DEBUG = False


APP_CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
