from flask import Blueprint



bp_auth = Blueprint('bp_auth',__name__,template_folder='templates',\
    static_folder='static', static_url_path='/auth/static')

blueprint_name = "bp_auth"  # The name of the module's blueprint
module_name = "auth"  # The name of the module

# URLS DICTIONARY
auth_urls = {
    'login': 'bp_auth.login',
    'users': 'bp_auth.users',
    'create': 'bp_auth.create_user',
    'edit': 'bp_auth.edit_user',
    'delete': 'bp_auth.user_delete',
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

from . import views
from . import models

