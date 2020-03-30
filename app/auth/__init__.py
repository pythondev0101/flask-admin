from flask import Blueprint
from app import system_models

bp_auth = Blueprint('bp_auth',__name__,)

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

# GLOBAL VARIABLE CONTEXT FOR URL RETURN
context = {
    'title': 'Users',
    'system_models': system_models,
    'active': 'Users',
    'forms': {},
    'modal': False,
}

from . import routes
from . import models

