from flask import current_app
from app.core import CoreModule
from .models import AdminDashboard, AdminApp
from app.auth.models import User,Role



class AdminModule(CoreModule):
    module_name = 'admin'
    module_icon = 'fa-home'
    module_link = current_app.config['ADMIN']['HOME_URL']
    module_short_description = 'Administration'
    module_long_description = "Administration Dashboard and pages"
    models = [AdminDashboard, AdminApp, User, Role]
    version = '1.0'
    sidebar = {
        'DASHBOARDS': [
            AdminDashboard, AdminApp
        ],
        'SYSTEM MODELS': [
            User, Role
        ]
    }
    
    def to_dict(self):
        return dict(
            name=self.module_name,
            icon=self.module_icon,
            short_description=self.module_short_description,
            long_description=self.module_long_description,
        )