from ez2erp.admin import AdminApp
from .models import Product



class Inventory(AdminApp):
    name = 'inventory'
    icon = 'fa-home'
    link = 'bp_admin.dashboard'
    short_description = 'Inventory'
    long_description = """
        Inventory management software is a software system for tracking inventory levels, 
        orders, sales and deliveries.
    """
    models = [Product]
    version = 1.0
