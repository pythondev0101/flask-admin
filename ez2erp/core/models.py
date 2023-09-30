""" CORE MODELS """
import enum
from datetime import datetime
from ez2erp.db.models import BaseModel
from ez2erp.db.fields import TextField



# class Base(db.Document):
#     meta = {
#         'abstract': True
#     }

#     active = db.BooleanField(default=True)
#     created_at = db.DateTimeField(default=datetime.utcnow)
#     # TODO: updated_at = db.DateTimeField(default=datetime.utcnow, onupdate=datetime.utcnow)
#     updated_at = db.DateTimeField(default=datetime.utcnow)

#     # TODO: I relate na to sa users table 
#     # Sa ngayon i store nalang muna yung names kasi andaming error kapag foreign key
#     created_by = db.StringField()
#     updated_by = db.StringField()


class App(BaseModel):
    ez2collection = 'core_apps'
    ez2name = 'app'
    
    name = TextField()
    short_description = TextField()
    long_description = TextField()
    status = TextField()
    version = TextField()
    models = []
    

class Model(BaseModel):
    ez2collection = 'core_models'
    ez2name = 'model'
    
    name = TextField()
    description = TextField()
    # name = db.StringField()
    # module = db.ReferenceField('CoreModule', required=True)
    # admin_included = db.BooleanField(default=True)


class ModuleStatus(enum.Enum):
    installed = "Installed"
    uninstalled = "Not Installed"


# class CoreCustomer(Base):
#     meta = {
#         'collection': 'core_customers'
#     }

#     fname = db.StringField()
#     lname = db.StringField()
#     phone = db.StringField()
#     email = db.EmailField()
#     zip = db.IntField()
#     street = db.StringField()


# class CoreCity(Base):
#     meta = {
#         'collection': 'core_cities'
#     }

#     name = db.StringField()
#     province = db.ReferenceField('CoreProvince')


# class CoreProvince(Base):
#     meta = {
#         'collection': 'core_provinces'
#     }

#     name = db.StringField()


# class CoreLog(db.Document):
#     meta = {
#         'abstract': True
#     }

#     date = db.DateTimeField(default=datetime.utcnow)
#     description = db.StringField()
#     data = db.StringField()
