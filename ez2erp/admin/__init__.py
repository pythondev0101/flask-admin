from flask import Blueprint



bp_admin = Blueprint(
    'bp_admin',__name__,template_folder='templates',
    static_folder='static',static_url_path='/admin/static'
)

# URLS DICTIONARY
admin_urls = {
    'admin': 'bp_admin.dashboard',
}

# TEMPLATES DICTIONARY
admin_templates = {
    'index': 'admin/admin_dashboard.html',
}

from . import templating
from . import routes
from . import models
from . import views
from . import notifications
from .admin import AdminApp
