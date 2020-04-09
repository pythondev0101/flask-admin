""" MODULE: AUTH.FORMS"""
""" FLASK IMPORTS """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,DateTimeField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from datetime import datetime
"""--------------END--------------"""
from app.admin.forms import AdminField,AdminForm

class RoleCreateForm(FlaskForm,AdminForm):
    name = StringField('name', validators=[DataRequired()])
    created_at = DateTimeField('Created At',format='%Y-%m-%dT%H:%M:%S', validators = [DataRequired()],
                               default=datetime.today())

    a_name = AdminField('name','Role Name','text')

    create_fields = [
        [a_name]
    ]


# TODO: FOR FUTURE VERSION CHANGE THIS TO CLASS INHERITANCE
class UserEditForm(FlaskForm):
    active = BooleanField('Active', default=1)
    username = StringField('Username', validators=[DataRequired()])
    email = PasswordField('Email', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])

class UserForm(FlaskForm,AdminForm):
    active = BooleanField('Active',default=1)
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = PasswordField('Email', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])

    created_at = DateTimeField('Created At',format='%Y-%m-%dT%H:%M:%S', validators = [DataRequired()],
                               default=datetime.today())

    a_username = AdminField('username','Username','text')
    a_fname = AdminField('fname','First Name','text')
    a_lname = AdminField('lname','Last Name','text')
    a_email = AdminField('email','Email','email')
    a_password = AdminField('password','Password','password')

    create_fields = [
        [a_fname,a_lname,a_username],
        [a_email,a_password]
    ]

# AUTH.FORMS.LOGINFORM
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log in')

def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
        raise ValidationError('User exists, please use another username')


def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
        raise ValidationError('User exists, please use another email')

