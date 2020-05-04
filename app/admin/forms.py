""" Admin form """
from flask_wtf import FlaskForm
from wtforms import Field
from wtforms import widgets


class AdminIndexForm(FlaskForm):
    @property
    def index_headers(self):
        raise NotImplementedError('Must implement index_headers')

    @property
    def index_title(self):
        raise NotImplementedError('Must implement index_title')

    @property
    def index_message(self):
        raise NotImplementedError('Must implement index_message')

    @property
    def create_fields(self):
        raise NotImplementedError('Must implement create_fields')
    
    def __init__(self,*args,**kwargs):
        super(AdminIndexForm,self).__init__(*args,**kwargs)
        self.title = self.index_title


class AdminEditForm(FlaskForm):
    inlines = None

    @property
    def edit_title(self):
        raise NotImplementedError('Must implement edit_title')

    @property
    def edit_message(self):
        raise NotImplementedError('Must implement edit_message')

    @property
    def edit_fields(self):
        raise NotImplementedError('Must implement edit_fields')

    @property
    def fields_data(self):
        raise NotImplementedError('Must implement fields_data')


class AdminSelectField(object):
    def __init__(self, name, label, data):
        self.name = name
        self.label = label
        self.input_type = 'select'
        self.data = data


class AdminInlineForm(object):
    models = None

    @property
    def headers(self):
        raise NotImplementedError('Must implement headers')

    @property
    def title(self):
        raise NotImplementedError('Must implement title')

    @property
    def html(self):
        raise NotImplementedError('Must implement html')


class AdminField(Field):

    widget = widgets.TextInput()
    
    def __init__(self,input_type="text",*args, **kwargs):
        super(AdminField,self).__init__(*args,**kwargs)
        self.input_type = input_type
        self.label = kwargs.get('label')

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[0]
        elif self.data is None:
            self.data = ''

    def _value(self):
        return text_type(self.data) if self.data is not None else ''

