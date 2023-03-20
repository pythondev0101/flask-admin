""" MODULE: AUTH.MODELS """

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from ez2erp import MONGO, LOGIN_MANAGER, db 
from ez2erp.admin.models import Admin
from ez2erp.core.models import Base
from ez2erp.db.model import BaseModel
from ez2erp.db.fields import TextField



class User(UserMixin, BaseModel):
    collection = 'auth_users'

    username = TextField('Username')
    fname = TextField('First Name')
    lname = TextField('Last Name')
    password_hash = TextField()
    contact_no = TextField('Contact No.')
    email = TextField('Email')
    role = TextField('Role')
    image_path: str = 'img/user_default_image.png'


    def __init__(self, data=None):
        BaseModel.__init__(self, data=data)
        
        if data:
            self.username = data.get('username', '')
            self.fname = data.get('fname', '')
            self.lname = data.get('lname', '')
            self.contact_no = data.get('contact_no', '')
            self.password_hash = data.get('password_hash', '')
            self.email = data.get('email', '')
            self.role = data.get('role', 'member')
            self.image_path = data.get('image_path', 'img/user_default_image.png')


    def set_password(self, password):
        self.password = password
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def get_full_name(self):
        return self.fname + " " + self.lname


    @classmethod
    def find_by_username(cls, username):
        query = Model.find_one(cls, {'username': username})
        if query is None:
            return None
        print(query)
        return cls(data=query)


    @property
    def code(self):
        self._code = "{}-{}".format(type(self).__name__, self.username) 
        return self._code


    @property
    def full_name(self):
        return self.fname + " " + self.lname


@LOGIN_MANAGER.user_loader
def load_user(user_id):
    return User.query.retrieve(user_id)


# AUTH.MODEL.USER
# class User(UserMixin, Base, Admin):
#     meta = {
#         'collection': 'auth_users'
#     }
#     __tablename__ = 'auth_users'
#     __amname__ = 'user'	
#     __amicon__ = 'pe-7s-users'	
#     __amdescription__ = "Users"	
#     __view_url__ = 'bp_auth.users'

#     """ COLUMNS """
#     username = db.StringField(unique=True)
#     fname = db.StringField()
#     lname = db.StringField()
#     email = db.EmailField()
#     password_hash = db.StringField()
#     image_path = db.StringField(default="img/user_default_image.png")
#     permissions = db.ListField(db.ReferenceField('UserPermission'))
#     is_superuser = db.BooleanField(default=False)
#     role = db.ReferenceField('Role')
#     is_admin = db.BooleanField(default=False)

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

#     def __repr__(self):
#         return "<User {}>".format(self.username)


class UserPermission(db.Document):
    meta = {
        'collection': 'auth_user_permissions'
    }

    model = db.ReferenceField('CoreModel')
    read = db.BooleanField(default=True)
    create = db.BooleanField(default=False)
    write = db.BooleanField(default=False)
    doc_delete = db.BooleanField(default=False)


class Role(Base, Admin):
    meta = {
        'collection': 'auth_user_roles'
    }

    __tablename__ = 'auth_user_roles'
    __amname__ = 'role'
    __amicon__ = 'pe-7s-id'
    __amdescription__ = "Roles"
    __view_url__ = 'bp_auth.roles'

    """ COLUMNS """
    name = db.StringField()
    # permissions = db.ListField()


class RolePermission(db.Document):
    meta = {
        'collection': 'auth_role_permissions'
    }

    role = db.ReferenceField('Role')
    model = db.ReferenceField('CoreModel')
    read = db.BooleanField(default=True)
    create = db.BooleanField(default=False)
    write = db.BooleanField(default=False)
    doc_delete = db.BooleanField(default=False)

