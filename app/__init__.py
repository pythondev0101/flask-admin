"""
app/__init__.py
====================================
Create our application
"""

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

system_modules = []

context = {'system_modules': system_modules, 'module': '', 'active': '', 'errors': {}, 
        'create_modal': {}, 'header_color': "header_color15", 'sidebar_color': "sidebar_color15",
        'app_name':"HomeBest"}

def create_app(config_name):
    """
    Return the app at crenecreate nito ang application
    ----------
    config_name
        A string para kung ano ang gagamiting environment configuration(eg.develop,production,testing)
    """
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
        from app.admin import bp_admin
        """--------------END--------------"""

        """EDITABLE: REGISTER HERE THE MODULE BLUEPRINTS"""
        app.register_blueprint(bp_core, url_prefix='/')
        app.register_blueprint(bp_auth, url_prefix='/auth')
        app.register_blueprint(bp_admin, url_prefix='/admin')
        """--------------END--------------"""

        db.create_all()
        db.session.commit()

        """EDITABLE: INCLUDE HERE YOUR MODULE Admin models FOR ADMIN TEMPLATE"""
        from app.admin.admin import AdminModule

        modules = [AdminModule]
        """--------------END--------------"""
        
        _install_modules(modules)
    return app


def _install_modules(modules):
    """
    Tatanggap to ng list ng modules tapos iinsert nya sa database yung mga models o tables nila, \
        para malaman ng system kung ano yung mga models(eg. Users,Customers)
    Parameters
    ----------
    modules
        Listahan ng mga modules na iinstall sa system
    """

    from app.core.models import HomeBestModel,HomeBestModule
    
    module_count = 0

    for module in modules:
        system_modules.append({'name':module.module_name,'short_description': module.module_short_description,
        'long_description':module.module_long_description,'link': module.module_link,
        'icon': module.module_icon, 'models': []})
        
        # TODO: Iimprove to kasi kapag nag error ang isa damay lahat dahil sa last_id
        homebest_module = HomeBestModule.query.filter_by(name=module.module_name).first()
        last_id = 0
        if not homebest_module:
            new_module = HomeBestModule(module.module_name,module.module_short_description,module.version)
            new_module.long_description = module.module_long_description
            new_module.status = 'installed'
            db.session.add(new_module)
            db.session.commit()
            last_id = new_module.id

        model_count = 0

        for model in module.models:
            homebestmodel = HomeBestModel.query.filter_by(name=model.model_name).first()
            if not homebestmodel:
                new_model = HomeBestModel(model.model_name, last_id, model.model_description)
                db.session.add(new_model)
                db.session.commit()
            system_modules[module_count]['models'].append({'name':model.model_name,'icon': model.model_icon,
            'functions': []})
            
            for function in model.functions:
                for function_name, function_link in function.items():
                    system_modules[module_count]['models'][model_count]['functions'].append({
                        function_name:function_link
                    })
        
            model_count = model_count + 1

        if len(module.no_admin_models) > 0 :

            for xmodel in module.no_admin_models:
                homebestmodel = HomeBestModel.query.filter_by(name=xmodel.model_name).first()
                if not homebestmodel:
                    new_model = HomeBestModel(xmodel.model_name, last_id, xmodel.model_description,False)
                    db.session.add(new_model)
                    db.session.commit()

        module_count = module_count + 1