""" CORE MODELS """
from app.admin.models import Admin
from datetime import datetime

from app import db
import enum


# MODEL.BASE
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # TODO: I relate na to sa users table 
    # Sa ngayon i store nalang muna yung names kasi andaming error kapag foreign key
    created_by = db.Column(db.String(64),nullable=True)
    updated_by = db.Column(db.String(64),nullable=True)

    def __init__(self):
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.active = 1


class CoreModel(Base):
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


class CoreModule(Base):
    __tablename__ = 'core_module'
    name = db.Column(db.String(64), nullable=False, server_default="")
    short_description = db.Column(db.String(64), nullable=False, server_default="")
    long_description = db.Column(db.String(255), nullable=False, server_default="")
    status = db.Column(db.Enum(ModuleStatus),default=ModuleStatus.uninstalled,nullable=False)
    version = db.Column(db.String(64), nullable=False, server_default="")
    models = db.relationship('CoreModel', cascade='all,delete', backref="core_module")

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
    province = db.relationship("CoreProvince",backref='city')


class CoreProvince(Base):
    __tablename__ = 'core_province'
    id = db.Column(db.Integer,primary_key=True, autoincrement=False)
    name = db.Column(db.String(64), nullable=False,default="")


class CoreLog(db.Model):
    __abstract__ = True

    """ COLUMNS """
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(500),nullable=True)
    data = db.Column(db.String(500),nullable=True)
