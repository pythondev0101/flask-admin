""" THIS IS FOR ADMIN MODELS """

from app.auth.models import User


class AdminModule():
    module_name = 'admin'
    module_icon = 'fa-home'
    module_link = 'bp_admin.dashboard'
    module_description = 'Administrator'
    models = [User]