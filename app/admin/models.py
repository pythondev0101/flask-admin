""" ADMIN MODELS"""


class Admin(object):
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



