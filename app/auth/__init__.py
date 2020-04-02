from flask import Blueprint
from app import system_modules

bp_auth = Blueprint('bp_auth',__name__,)

blueprint_name = "bp_auth"  # The name of the module's blueprint
module_name = "auth"  # The name of the module

# URLS DICTIONARY
auth_urls = {
    'login': 'bp_auth.login',
    'index': 'bp_auth.index',
    'create': 'bp_auth.user_create',
    'edit': 'bp_auth.user_edit',
    'delete': 'bp_auth.user_delete',
}

# TEMPLATES DICTIONARY
auth_templates = {
    'login': 'auth/user_login.html',
    'index': 'auth/user_index.html',
    'edit': 'auth/user_edit.html',
}


from . import routes
from . import models



