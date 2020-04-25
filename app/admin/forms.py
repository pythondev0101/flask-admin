""" Admin form """


class AdminIndexForm(object):
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

    def __int__(self):
        self.title = self.index_title


class AdminEditForm(object):
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


class AdminCreateField(object):
    def __init__(self, name, label, input_type):
        self.name = name
        self.label = label
        self.input_type = input_type


class AdminSelectField(object):
    def __init__(self, name, label, data):
        self.name = name
        self.label = label
        self.input_type = 'select'
        self.data = data


class AdminEditField(object):
    def __init__(self, name, label, input_type,value):
        self.name = name
        self.label = label
        self.input_type = input_type
        self.value = value


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







