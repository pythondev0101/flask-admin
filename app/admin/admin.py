""" THIS IS FOR ADMIN MODELS """

from app.auth.models import User,Role
from app.core import CoreModule


class AdminModule(CoreModule):
    module_name = 'admin'
    module_icon = 'fa-home'
    module_link = 'bp_admin.dashboard'
    module_short_description = 'Administration'
    module_long_description = "Administration Dashboard and pages"
    models = [User, Role]
    version = '1.0'