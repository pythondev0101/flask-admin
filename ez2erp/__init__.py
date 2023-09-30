"""
app/__init__.py
====================================
Create our application
"""
from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from config import APP_CONFIG

# DEVELOPERS-NOTE: -INCLUDE YOUR IMPORTS HERE-

#                  -END-

MONGO = PyMongo()
CSRF = CSRFProtect()
APP_CORS = CORS()
LOGIN_MANAGER = LoginManager()
APPS = []
CONTEXT = {
    'system_modules': []
}


def internal_server_error(e):
    from flask import render_template
    return render_template('admin/internal_server_error.html'), 500


def create_app(config_name):
    """
    Return the app at crenecreate nito ang application
    ----------
    config_name
        A string para kung ano ang gagamiting environment configuration(eg.develop,production,testing)
    """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(APP_CONFIG[config_name])
    app.register_error_handler(500, internal_server_error)

    MONGO.init_app(app)
    LOGIN_MANAGER.init_app(app)
    APP_CORS.init_app(app)
    CSRF.init_app(app)
    # DEVELOPERS-NOTE: -INITIALIZE YOUR IMPORTS HERE-

    #                    -END-

    LOGIN_MANAGER.login_view = 'bp_auth.login'
    LOGIN_MANAGER.login_message = "You must be logged in to access this page."


    # DEVELOPERS-NOTE: -IMPORT HERE THE SYSTEM MODULES-
    from ez2erp.core import bp_core
    from ez2erp.auth import bp_auth
    from ez2erp.admin import bp_admin
    from ez2erp.home import bp_home
    from upec import bp_upec
    #                   -END-

    # DEVELOPERS-NOTE: -REGISTER HERE THE MODULE BLUEPRINTS-
    app.register_blueprint(bp_core, url_prefix='/core')
    app.register_blueprint(bp_admin, url_prefix='/admin')
    app.register_blueprint(bp_auth, url_prefix='/auth')
    app.register_blueprint(bp_home, url_prefix='/')
    app.register_blueprint(bp_upec, url_prefix='/upec')
    #               -END-
    
    with app.app_context():
        # DEVELOPERS-NOTE: -INCLUDE HERE YOUR MODULE Admin models FOR ADMIN TEMPLATE-
        from ez2erp.social.app import Social
        from ez2erp.inventory.app import Inventory
        from upec.app import Upec
        #                  -END-

        # DEVELOPERS-NOTE: -APPEND YOUR MODULE HERE-
        APPS.append(Inventory)
        APPS.append(Social)
        APPS.append(Upec)
        #                  -END-

    return app
