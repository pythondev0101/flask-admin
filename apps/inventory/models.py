from ez2erp.db.models import BaseModel
from ez2erp.db.fields import TextField



class Product(BaseModel):
    ez2collection = 'inventory_products'
    ez2name = 'product'
    name = TextField()
