""" CORE MODELS """
from mongoengine.document import Document
from app.admin.models import Admin
from datetime import datetime

from app import db
import enum



class Base(db.Document):
    meta = {
        'abstract': True
    }

    active = db.BooleanField(default=True)
    created_at = db.DateTimeField(default=datetime.utcnow)
    # TODO: updated_at = db.DateTimeField(default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)

    # TODO: I relate na to sa users table 
    # Sa ngayon i store nalang muna yung names kasi andaming error kapag foreign key
    created_by = db.StringField()
    updated_by = db.StringField()


class CoreModel(Base):
    meta = {
        'collection': 'core_models'
    }

    name = db.StringField()
    module = db.ReferenceField('CoreModule', required=True)
    description = db.StringField()
    admin_included = db.BooleanField(default=True)


class ModuleStatus(enum.Enum):
    installed = "Installed"
    uninstalled = "Not Installed"


class CoreModule(Base):
    meta = {
        'collection': 'core_modules'
    }

    name = db.StringField()
    short_description = db.StringField()
    long_description = db.StringField()
    status = db.StringField()
    version = db.StringField()
    models = db.ListField(db.ReferenceField('CoreModel'))


class CoreCustomer(Base):
    meta = {
        'collection': 'core_customers'
    }

    fname = db.StringField()
    lname = db.StringField()
    phone = db.StringField()
    email = db.EmailField()
    zip = db.IntField()
    street = db.StringField()


class CoreCity(Base):
    meta = {
        'collection': 'core_cities'
    }

    name = db.StringField()
    province = db.ReferenceField('CoreProvince')


class CoreProvince(Base):
    meta = {
        'collection': 'core_provinces'
    }

    name = db.StringField()


class CoreLog(db.Document):
    meta = {
        'abstract': True
    }

    date = db.DateTimeField(default=datetime.utcnow)
    description = db.StringField()
    data = db.StringField()
