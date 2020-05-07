""" MODULE: AUTH.FORMS"""
""" FLASK IMPORTS """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from datetime import datetime
"""--------------END--------------"""

from app.admin.forms import AdminIndexForm,AdminEditForm, AdminInlineForm, AdminField


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
    username = AdminField(label='Username', validators=[DataRequired()],input_type='text')
    email = AdminField(label='Email', validators=[DataRequired()],input_type='text')
    fname = AdminField(label='First Name', validators=[DataRequired()],input_type='text')
    lname = AdminField(label='Last Name', validators=[DataRequired()],input_type='text')
    
    def edit_fields(self):
        return [[self.fname, self.lname],[self.username,self.email]]

    edit_title = "Edit User"
    edit_message = "message"

    permission_inline = PermissionInlineForm()
    model_inline = ModelInlineForm()
    inlines = [permission_inline,model_inline]


class UserForm(AdminIndexForm):
    username = AdminField(label='Username',input_type='text',validators=[DataRequired()])
    email = AdminField(label='Email', input_type='email',required=False)
    fname = AdminField(label='First Name', input_type='text',validators=[DataRequired()])
    lname = AdminField(label='Last Name', input_type='text',validators=[DataRequired()])

    def create_fields(self):
        return [[self.fname, self.lname],[self.username,self.email]]

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