from app.core.core import CoreModule
from .models import *


class BDSModule(CoreModule):
    module_name = 'bds'
    module_icon = 'fa-map'
    module_link = 'bp_bds.dashboard'
    module_short_description = 'BDS'
    module_long_description = "Administrator Dashboard and pages"
    models = [Delivery, Area, Subscriber, Messenger]
    no_admin_models = []
    version = '1.0'