from flask import current_app
from app.auth.models import User,Role
from app.core import CoreModule



class AdminModule(CoreModule):
    module_name = 'admin'
    module_icon = 'fa-home'
    module_link = current_app.config['ADMIN']['HOME_URL']
    module_short_description = 'Administration'
    module_long_description = "Administration Dashboard and pages"
    models = [User, Role]
    version = '1.0'