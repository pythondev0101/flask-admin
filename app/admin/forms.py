""" Admin form """


class AdminForm(object):
    @property
    def create_fields(self):
        raise NotImplementedError('Must implement create_fields')


class AdminField(object):
    def __init__(self, name, label, input_type):
        self.name = name
        self.label = label
        self.input_type = input_type


class AdminSelectField(object):
    def __init__(self, name, label, input_type, data):
        self.name = name
        self.label = label
        self.input_type = input_type
        self.data = data
