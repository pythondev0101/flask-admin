""" CORE MODELS """
from datetime import datetime

from app import db
import enum


# MODEL.BASE
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, nullable=False, default="1")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self):
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.active = 1


class HomeBestModel(Base):
    __tablename__ = 'core_model'
    name = db.Column(db.String(64), nullable=False, server_default="")
    module_id = db.Column(db.Integer, db.ForeignKey('core_module.id'))
    description = db.Column(db.String(128), nullable=True, server_default="")
    admin_included = db.Column(db.Boolean,default="1")

    def __init__(self,name,module_id,description,admin_included=True):
        Base.__init__(self)
        self.name = name
        self.module_id = module_id
        self.description = description
        self.admin_included = admin_included


class ModuleStatus(enum.Enum):
    installed = "Installed"
    uninstalled = "Not Installed"


class HomeBestModule(Base):
    __tablename__ = 'core_module'
    name = db.Column(db.String(64), nullable=False, server_default="")
    short_description = db.Column(db.String(64), nullable=False, server_default="")
    long_description = db.Column(db.String(255), nullable=False, server_default="")
    status = db.Column(db.Enum(ModuleStatus),default=ModuleStatus.uninstalled,nullable=False)
    version = db.Column(db.String(64), nullable=False, server_default="")
    models = db.relationship('HomeBestModel', cascade='all,delete', backref="homebestmodule")

    def __init__(self,name,short_description,version):
        Base.__init__(self)
        self.name = name
        self.short_description = short_description
        self.version = version


class CoreCustomer(Base):
    __abstract__ = True
    fname = db.Column(db.String(64), nullable=False, default="")
    lname = db.Column(db.String(64), nullable=False, default="")
    phone = db.Column(db.String(64), nullable=True, default="")
    email = db.Column(db.String(64), nullable=True, unique=True)
    zip = db.Column(db.Integer,nullable=True,default=None)
    street = db.Column(db.String(64), nullable=True,default="")


class CoreCity(Base):
    __tablename__ = 'core_city'
    id = db.Column(db.Integer,primary_key=True, autoincrement=False)
    name = db.Column(db.String(64), nullable=False,default="")
    province_id = db.Column(db.Integer, db.ForeignKey('core_province.id'), nullable=True)
    province = db.relationship("CoreProvince")


class CoreProvince(Base):
    __tablename__ = 'core_province'
    id = db.Column(db.Integer,primary_key=True, autoincrement=False)
    name = db.Column(db.String(64), nullable=False,default="")
