""" ADMIN MODELS"""


class Admin(object):
    @property
    def index_fields(self):
        raise NotImplementedError('Must implement index_fields')

    @property
    def index_title(self):
        raise NotImplementedError('Must implement index_title')

    @property
    def index_message(self):
        raise NotImplementedError('Must implement index_message')

    @property
    def model_name(self):
        raise NotImplementedError('Must implement model_name')

    @property
    def model_icon(self):
        raise NotImplementedError('Must implement model_icon')

    @property
    def model_description(self):
        raise NotImplementedError('Must implement model_description')

    @property
    def functions(self):
        raise NotImplementedError('Must implement functions')

    def __int__(self):
        self.title = self.index_title


