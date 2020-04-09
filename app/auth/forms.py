""" MODULE: AUTH.FORMS"""
""" FLASK IMPORTS """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,DateTimeField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from datetime import datetime
"""--------------END--------------"""


class RoleCreateForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    created_at = DateTimeField('Created At',format='%Y-%m-%dT%H:%M:%S', validators = [DataRequired()],
                               default=datetime.today())


# TODO: FOR FUTURE VERSION CHANGE THIS TO CLASS INHERITANCE
class UserEditForm(FlaskForm):
    active = BooleanField('Active', default=1)
    username = StringField('Username', validators=[DataRequired()])
    email = PasswordField('Email', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])

class UserForm(FlaskForm):
    active = BooleanField('Active',default=1)
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = PasswordField('Email', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])

    created_at = DateTimeField('Created At',format='%Y-%m-%dT%H:%M:%S', validators = [DataRequired()],
                               default=datetime.today())


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

