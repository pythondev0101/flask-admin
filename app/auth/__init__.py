from flask import Blueprint

bp_auth = Blueprint('bp_auth',__name__,)

# URLS DICTIONARY
auth_urls = {
    'login': 'bp_auth.login',
    'index': 'bp_auth.index',
    'create': 'bp_auth.user_create',
}

# TEMPLATES DICTIONARY
auth_templates = {
    'login': 'auth/user_login.html',
    'index': 'auth/user_index.html',
}

from . import routes
from . import models

