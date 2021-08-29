""" MODULE: AUTH.MODELS """
""" FLASK IMPORTS """
from enum import unique
from flask_login import UserMixin

"""--------------END--------------"""

""" PYTHON IMPORTS """
from werkzeug.security import generate_password_hash, check_password_hash

"""--------------END--------------"""

""" APP IMPORTS  """
from app import login_manager,db
from app.admin.models import Admin
from app.core.models import Base
"""--------------END--------------"""
from mongoengine.document import Document



# AUTH.MODEL.USER
class User(UserMixin, Base, Admin):
    meta = {
        'collection': 'auth_users'
    }
    __tablename__ = 'auth_users'
    __amname__ = 'user'	
    __amicon__ = 'pe-7s-users'	
    __amdescription__ = "Users"	
    __view_url__ = 'bp_auth.users'

    """ COLUMNS """
    username = db.StringField(unique=True)
    fname = db.StringField()
    lname = db.StringField()
    email = db.EmailField()
    password_hash = db.StringField()
    image_path = db.StringField(default="img/user_default_image.png")
    permissions = db.ListField(db.ReferenceField('UserPermission'))
    is_superuser = db.BooleanField(default=False)
    role = db.ReferenceField('Role')
    is_admin = db.BooleanField(default=False)

    @classmethod
    def authenticate(cls, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        
        if not username or not password:
            return None

        user = cls.objects(username=username).first()
        if not user or not user.check_password(password):
            return None

        return user

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.username)
    
    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            create_at=self.created_at,
            )

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


@login_manager.user_loader
def load_user(user_id):
    return User.objects.get(id=user_id)