from flask import Flask,g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
# LOCAL IMPORTS
from config import app_config

# INITIALIZE FLASK IMPORTS
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
login_manager = LoginManager()

system_modules = {}

context = {'system_modules': system_modules, 'module': '', 'active': '', 'errors': {}, 
        'create_modal': {}, 'header_color': "header_color15", 'sidebar_color': "sidebar_color15",
        'app_name':"HomeBest"}

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    CORS(app)
    csrf.init_app(app)

    login_manager.login_view = 'bp_auth.login'
    login_manager.login_message = "You must be logged in to access this page."

    with app.app_context():

        """EDITABLE: IMPORT HERE THE SYSTEM MODULES  """
        from app.core import bp_core
        from app.auth import bp_auth
        from app.admin import bp_admin,AdminModule
        """--------------END--------------"""

        """EDITABLE: REGISTER HERE THE MODULE BLUEPRINTS"""
        app.register_blueprint(bp_core, url_prefix='/')
        app.register_blueprint(bp_auth, url_prefix='/auth')
        app.register_blueprint(bp_admin, url_prefix='/admin')
        """--------------END--------------"""
        db.create_all()
        db.session.commit()

        """EDITABLE: INCLUDE HERE YOUR MODULE Admin models FOR ADMIN TEMPLATE"""
        modules = [AdminModule]
        """--------------END--------------"""
        create_modules(modules)

    return app


def create_modules(modules):
    from app.core.models import HomeBestModel

    for module in modules:
        system_modules[module.module_name] = {'description': module.module_description,
        'link': module.module_link,'icon': module.module_icon, 'models': {}}

        for model in module.models:
            homebestmodel = HomeBestModel.query.filter_by(name=model.model_name).first()
            if not homebestmodel:
                new_model = HomeBestModel(model.model_name, module.module_name, model.model_description)
                db.session.add(new_model)
                db.session.commit()
            system_modules[module.module_name]['models'][model.model_name] = {'icon': model.model_icon,
            'functions': {}}
            for function_name, function_link in model.functions.items():
                system_modules[module.module_name]['models'][model.model_name]['functions'][function_name] = function_link

    print(system_modules)


