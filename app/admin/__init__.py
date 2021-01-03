from flask import Blueprint



bp_admin = Blueprint(
    'bp_admin',__name__,template_folder='templates',
    static_folder='static',static_url_path='/admin/static'
    )

blueprint_name = "bp_admin"  # The name of the module's blueprint

module_name = "admin" # The name of the module

# URLS DICTIONARY
admin_urls = {
    'admin': 'bp_admin.dashboard',
}

# TEMPLATES DICTIONARY
admin_templates = {
    'index': 'admin/admin_dashboard.html',
}

from . import routes
from . import models
