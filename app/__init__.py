from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_login import LoginManager

db = SQLAlchemy()
r = FlaskRedis()
login_manager = LoginManager()
login_manager.login_view = 'bp_auth.login'

system_modules = {}

# GLOBAL VARIABLE CONTEXT FOR URL RETURN
context = {
    'title': '',
    'system_modules': system_modules,
    'module':'',
    'active': '',
    'forms': {},
    'modal': False,
}

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    r.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        """EDITABLE: IMPORT HERE THE SYSTEM MODULES  """
        from app import core
        from app import auth
        from app import admin
        """--------------END--------------"""

        """EDITABLE: INCLUDE HERE YOUR MODULE Admin models FOR ADMIN TEMPLATE"""
        modules = [admin.AdminModule]
        """--------------END--------------"""

        for module in modules:
            system_modules[module.module_name] = {'description': module.module_description, 'link': module.module_link,
                                                  'icon': module.module_icon, 'models': {}}
            for model in module.models:
                system_modules[module.module_name]['models'][model.model_name] = {'icon':model.model_icon,'functions': {}}
                for function_name, function_link in model.functions.items():
                    system_modules[module.module_name]['models'][model.model_name]['functions'][function_name] = function_link

        """EDITABLE: REGISTER HERE THE MODULE BLUEPRINTS"""
        app.register_blueprint(core.bp_core,url_prefix='/')
        app.register_blueprint(auth.bp_auth,url_prefix='/auth')
        app.register_blueprint(admin.bp_admin,url_prefix='/admin')
        """--------------END--------------"""

        db.create_all()
        return app
# GLOBAL APP INSTANCE
app = create_app()