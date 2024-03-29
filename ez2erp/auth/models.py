""" MODULE: AUTH.MODELS """

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from ez2erp import LOGIN_MANAGER
from ez2erp.db.models import BaseModel
from ez2erp.db import fields
from ez2erp.admin.templating import SidebarItem



class User(UserMixin, BaseModel):
    ez2collection = 'auth_users'
    ez2name = 'user'
    ez2sidebar = [
        SidebarItem(
            name="Users",
            link="bp_admin.users"
        )
    ]

    username = fields.TextField("Username")
    fname = fields.TextField('First Name')
    lname = fields.TextField('Last Name')
    password_hash = fields.TextField()
    contact_no = fields.TextField('Contact No.')
    email = fields.TextField("Email")
    role = fields.ReferenceField('Role')
    image_path: str = 'img/user_default_image.png'
    status = fields.TextField()
    

    @property
    def full_name(self):
        return self.fname + " " + self.lname


    def set_password(self, password):
        self.password = password
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(BaseModel):
    ez2collection = 'auth_roles'
    ez2sidebar = [
        SidebarItem(
            name="Roles",
            link="bp_admin.roles"
        )
    ]

    name = fields.TextField('Name') 
    description = fields.TextField('Description')
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

