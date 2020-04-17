from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS

csrf = CSRFProtect()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'bp_auth.login'

system_modules = {}

# GLOBAL VARIABLE CONTEXT FOR URL RETURN
context = {
    'system_modules': system_modules,
    'module': '',
    'active': '',
    'errors': {},
    'create_modal': {},
}


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    CORS(app)
    csrf.init_app(app)

    with app.app_context():

        """EDITABLE: IMPORT HERE THE SYSTEM MODULES  """
        from app import core
        from app import auth
        from app import admin
        """--------------END--------------"""

        """EDITABLE: REGISTER HERE THE MODULE BLUEPRINTS"""
        app.register_blueprint(core.bp_core, url_prefix='/')
        app.register_blueprint(auth.bp_auth, url_prefix='/auth')
        app.register_blueprint(admin.bp_admin, url_prefix='/admin')
        """--------------END--------------"""

        db.create_all()
        db.session.commit()

        """EDITABLE: INCLUDE HERE YOUR MODULE Admin models FOR ADMIN TEMPLATE"""
        modules = [admin.AdminModule]
        """--------------END--------------"""

        from app.core.models import HomeBestModel

        for module in modules:
            system_modules[module.module_name] = {'description': module.module_description, 'link': module.module_link,
                                                  'icon': module.module_icon, 'models': {}}
            for model in module.models:
                homebestmodel = HomeBestModel.query.filter_by(name=model.model_name).first()
                if not homebestmodel:
                    new_model = HomeBestModel(model.model_name,module.module_name,model.model_description)
                    db.session.add(new_model)
                    db.session.commit()
                # context['permissions'][model.model_name] = {"read":False,"write":False,"delete":False}
                system_modules[module.module_name]['models'][model.model_name] = {'icon':model.model_icon,'functions': {}}
                for function_name, function_link in model.functions.items():
                    system_modules[module.module_name]['models'][model.model_name]['functions'][function_name] = function_link

    return app


# GLOBAL APP INSTANCE
name = "HomeBest"
app = create_app()
