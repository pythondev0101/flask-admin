from flask import Blueprint
from app import context

bp_admin = Blueprint('bp_admin',__name__,template_folder='templates')

blueprint_name = "bp_admin"  # The name of the module's blueprint
module_name = "admin" # The name of the module

# URLS DICTIONARY
admin_urls = {
    'admin': 'bp_admin.index',
}

# TEMPLATES DICTIONARY
admin_templates = {
    'index': 'admin/admin_dashboard.html',
}

context['title'] = 'Admin'
context['module'] = 'admin'

from . import routes
from . import models


""" THIS IS FOR ADMIN MODELS """

from app.auth.models import Role,User


class AdminModule():
    module_name = 'admin'
    module_icon = 'fa-home'
    module_link = 'bp_admin.index'
    module_description = 'Administrator'
    models = [User,Role]
