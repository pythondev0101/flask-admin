from flask import Blueprint

bp_admin = Blueprint('bp_admin',__name__,)

# URLS DICTIONARY
admin_urls = {
    'admin': 'bp_admin.index',
}

# TEMPLATES DICTIONARY
admin_templates = {
    'index': 'admin/admin_index.html',
}

from . import routes

