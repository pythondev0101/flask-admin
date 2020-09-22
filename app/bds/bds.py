from app.core.core import CoreModule


class BDSModule(CoreModule):
    module_name = 'bds'
    module_icon = 'fa-map'
    module_link = 'bp_bds.dashboard'
    module_short_description = 'BDS'
    module_long_description = "Administrator Dashboard and pages"
    models = []
    no_admin_models = []
    version = '1.0'