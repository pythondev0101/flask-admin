""" MODULE: AUTH.FORMS"""
""" FLASK IMPORTS """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, SelectField, \
    IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from datetime import datetime
"""--------------END--------------"""

from app.admin.forms import AdminCreateField, AdminIndexForm, AdminSelectField,AdminEditForm,\
    AdminEditField,AdminInlineForm


# class RoleCreateForm(FlaskForm, AdminIndexForm):
#     name = StringField('name', validators=[DataRequired()])
#     created_at = DateTimeField('Created At', format='%Y-%m-%dT%H:%M:%S', validators=[DataRequired()],
#                                default=datetime.today())

#     a_name = AdminCreateField('name', 'Role Name', 'text')

#     create_fields = [
#         [a_name]
#     ]

#     index_headers = ['name', 'Created']
#     index_title = "All Roles"
#     index_message = "Message"
#     title = index_title


class PermissionInlineForm(AdminInlineForm):
    headers =['Model','Read','create','write','delete','Remove']
    title = "Edit Rights"
    html = 'auth/permission_inline.html'

class ModelInlineForm(AdminInlineForm):
    headers = ['Model','Read','create','write','delete','add']
    title = "Add Rights"
    html = 'auth/model_inline.html'


# TODO: FOR FUTURE VERSION CHANGE THIS TO CLASS INHERITANCE
class UserEditForm(AdminEditForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    # role_id = IntegerField('Role')

    a_username = AdminEditField('username', 'Username', 'text',username)
    a_fname = AdminEditField('fname', 'First Name', 'text',fname)
    a_lname = AdminEditField('lname', 'Last Name', 'text',lname)
    a_email = AdminEditField('email', 'Email', 'email',email)
    # a_role = AdminSelectField('role_id', 'Role', 'select', Role)

    edit_fields = [
        [a_fname, a_lname, a_username],
        [a_email]
    ]

    edit_title = "Edit User"
    edit_message = "message"

    permission_inline = PermissionInlineForm()
    model_inline = ModelInlineForm()
    inlines = [permission_inline,model_inline]

class UserForm(AdminIndexForm):
    active = BooleanField('Active', default=1)
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = PasswordField('Email', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])

    # role_id = StringField('Role')

    created_at = DateTimeField('Created At', format='%Y-%m-%dT%H:%M:%S', validators=[DataRequired()],
                               default=datetime.today())

    a_username = AdminCreateField('username', 'Username', 'text')
    a_fname = AdminCreateField('fname', 'First Name', 'text')
    a_lname = AdminCreateField('lname', 'Last Name', 'text')
    a_email = AdminCreateField('email', 'Email', 'email')
    a_password = AdminCreateField('password', 'Password', 'password')
    # a_role = AdminSelectField('role_id', 'Role', 'select', Role)

    create_fields = [
        [a_fname, a_lname, a_username],
        [a_email, a_password]
    ]

    index_headers = ['Username', 'First name', 'last name', 'email']
    index_title = "Users"
    index_message = "Message"


class UserPermissionForm(AdminIndexForm):
    index_headers = ['Username', 'Name', 'Model', 'Read','create', 'Write', 'Delete']
    index_title = "User Permissions"
    index_message = "Message"


# AUTH.FORMS.LOGINFORM
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log in')