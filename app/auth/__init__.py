from flask import Blueprint

bp_auth = Blueprint('bp_auth',__name__,template_folder='templates')

blueprint_name = "bp_auth"  # The name of the module's blueprint
module_name = "auth"  # The name of the module

# URLS DICTIONARY
auth_urls = {
    'login': 'bp_auth.login',
    'index': 'bp_auth.index',
    'create': 'bp_auth.user_create',
    'edit': 'bp_auth.user_edit',
    'delete': 'bp_auth.user_delete',
    'user_add_permission': 'bp_auth.user_add_permission',
    'user_permission_index': 'bp_auth.user_permission_index',
    'role_index': 'bp_auth.role_index',
}

# TEMPLATES DICTIONARY
auth_templates = {
    'login': 'auth/user_login.html',
    'edit': 'auth/user_edit.html',
    'user_permission_index': 'auth/user_permission_index.html',
    'role_index': 'auth/role_index.html',
}


from . import routes
from . import models
from . import api


