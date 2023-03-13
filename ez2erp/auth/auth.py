from ez2erp.core import CoreModule



class AuthModule(CoreModule):
    background_app = True
    module_name = 'auth'
    module_icon = None
    module_link = None
    module_short_description = 'Authentication'
    module_long_description = "Authentication and permissions"
    models = []
    version = '1.0'
