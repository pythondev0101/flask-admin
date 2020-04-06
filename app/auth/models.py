""" MODULE: AUTH.MODELS """
""" FLASK IMPORTS """
from flask_login import UserMixin

"""--------------END--------------"""

""" PYTHON IMPORTS """
from werkzeug.security import generate_password_hash, check_password_hash

"""--------------END--------------"""

""" APP IMPORTS  """
from app import db
from app.core.models import Base
"""--------------END--------------"""


# AUTH.MODEL.USER
class User(UserMixin, Base):
    __tablename__ = 'auth_user'

    username = db.Column(db.String(64), nullable=False, index=True, unique=True)
    fname = db.Column(db.String(64), nullable=False, server_default="")
    lname = db.Column(db.String(64), nullable=False, server_default="")
    email = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    image_path = db.Column(db.String(64),nullable=False)
    permissions = db.relationship('UserPermission',cascade='all,delete',backref="user")
    role_id = db.Column(db.Integer,db.ForeignKey('auth_role.id'))
    role = db.relationship('Role',cascade='all,delete',backref="userrole")

    def __init__(self):
        Base.__init__(self)
        self.image_path = "img/user_default_image.png"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.username)


class UserPermission(db.Model):
    __tablename__ = 'auth_user_permission'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer,db.ForeignKey('auth_user.id'))
    model_id = db.Column(db.Integer,db.ForeignKey('core_model.id'))
    model = db.relationship('HomeBestModel',cascade='all,delete',backref="userpermission")
    read = db.Column(db.Boolean, nullable=False, default="1")
    write = db.Column(db.Boolean, nullable=False, default="1")
    delete = db.Column(db.Boolean, nullable=False, default="1")


class Role(Base):
    __tablename__ = 'auth_role'
    name = db.Column(db.String(64), nullable=False)


class RolePermission(db.Model):
    __tablename__ = 'auth_role_permission'
    id = db.Column(db.Integer, primary_key=True)

    role_id = db.Column(db.Integer,db.ForeignKey('auth_role.id'))
    model_id = db.Column(db.Integer,db.ForeignKey('core_model.id'))
    model = db.relationship('HomeBestModel',cascade='all,delete',backref="rolepermission")
    read = db.Column(db.Boolean, nullable=False, default="1")
    write = db.Column(db.Boolean, nullable=False, default="1")
    delete = db.Column(db.Boolean, nullable=False, default="1")
