"""Base class for modules"""


class CoreModule:

    no_admin_models = []

    @property
    def module_name(self):
        raise NotImplementedError('Must implement module_name')

    @property
    def module_short_description(self):
        raise NotImplementedError('Must implement module_short_description')

    @property
    def module_long_description(self):
        raise NotImplementedError('Must implement module_long_description')

    @property
    def module_link(self):
        raise NotImplementedError('Must implement module_link')

    @property
    def module_icon(self):
        raise NotImplementedError('Must implement module_icon')

    @property
    def models(self):
        raise NotImplementedError('Must implement models')

    @property
    def version(self):
        raise NotImplementedError('Must implement version')