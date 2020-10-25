from flask_wtf import FlaskForm
from app.admin.forms import AdminIndexForm,AdminEditForm, AdminInlineForm, AdminField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo


class SubscriberForm(AdminIndexForm):
    from .models import Area

    index_headers = ['First name','Last name']
    index_title = "Subscribers"

    fname = AdminField(label="First name",validators=[DataRequired()])
    lname = AdminField(label="Last name",validators=[DataRequired()])
    email = AdminField(label="Email Address",required=False)
    address = AdminField(label="Address",required=False)
    longitude = AdminField(label="Longitude", required=False)
    latitude = AdminField(label="Latitude", required=False)

    area_id = AdminField(label="Area", validators=[DataRequired()], model=Area)

    def create_fields(self):
        return [
            [self.fname,self.lname],[self.email,self.address],[self.longitude,self.latitude],[self.area_id]
            ]


class MessengerForm(AdminIndexForm):
    from .models import Area
    
    index_headers = ['Username', 'First name', 'last name', 'email']
    index_title = "Messengers"

    username = AdminField(label='Username', validators=[DataRequired()])
    email = AdminField(label='Email', input_type='email',required=False)
    fname = AdminField(label='First Name', validators=[DataRequired()])
    lname = AdminField(label='Last Name', validators=[DataRequired()])
    area_id = AdminField(label="Area", validators=[DataRequired()], model=Area)

    def create_fields(self):
        return [[self.fname, self.lname],[self.username,self.email], [self.area_id]]


class AreaForm(AdminIndexForm):
    index_headers = ['Name', 'code','description']
    index_title = "Areas"

    name = AdminField(label="Name",validators=[DataRequired()])
    code = AdminField(label="Code",validators=[DataRequired()])
    description = AdminField(label="Description", required=False)

    def create_fields(self):
        return [
            [self.name, self.code],[self.description]
        ]


class AreaCreateForm(FlaskForm):
    name = AdminField(label="Name",validators=[DataRequired()])
    code = AdminField(label="Code",validators=[DataRequired()])
    description = AdminField(label="Description", required=False)
