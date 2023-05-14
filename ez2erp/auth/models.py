""" MODULE: AUTH.MODELS """

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from ez2erp import LOGIN_MANAGER
from ez2erp.db.models import BaseModel
from ez2erp.db import fields



class User(UserMixin, BaseModel):
    ez2collection = 'auth_users'
    username = fields.TextField()
    fname = fields.TextField('First Name')
    lname = fields.TextField('Last Name')
    password_hash = fields.TextField()
    contact_no = fields.TextField('Contact No.')
    email = fields.TextField()
    role = fields.TextField()
    image_path: str = 'img/user_default_image.png'

    # def __init__(self, data=None):
    #     BaseModel.__init__(self, data=data)
        # 
        # if data:
        #     self.username = data.get('username')
        #     self.fname = data.get('fname')
        #     self.lname = data.get('lname')
        #     self.contact_no = data.get('contact_no')
        #     self.password_hash = data.get('password_hash')
        #     self.email = data.get('email')
        #     self.role = data.get('role', 'member')
        #     self.image_path = data.get('image_path', 'img/user_default_image.png')


    @property
    def full_name(self):
        return self.fname + " " + self.lname


    def set_password(self, password):
        self.password = password
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    # @classmethod
    # def find_by_username(cls, username):
    #     query = Model.find_one(cls, {'username': username})
    #     if query is None:
    #         return None
    #     print(query)
    #     return cls(data=query)


    # @property 
    # def code(self):
    #     self._code = "{}-{}".format(type(self).__name__, self.username) 
    #     return self._code


class Role(BaseModel):
    ez2collection = 'auth_roles'
    name = fields.TextField() 
    description = fields.TextField()
    # permissions = db.ListField()



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


class UserPermission(BaseModel):
    meta = {
        'collection': 'auth_user_permissions'
    }

    # model = db.ReferenceField('CoreModel')
    model = None
    read = fields.BooleanField()
    create = fields.BooleanField()
    write = fields.BooleanField()
    doc_delete = fields.BooleanField()


class RolePermission(BaseModel):
    ez2collection = 'auth_role_permissions'
    # role = db.ReferenceField('Role')
    role = None
    model = None
    read = fields.BooleanField()
    create = fields.BooleanField()
    write = fields.BooleanField()
    doc_delete = fields.BooleanField()

