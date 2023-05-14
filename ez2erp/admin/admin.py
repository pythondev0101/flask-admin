class AdminAppMeta(type):
    def __new__(cls, name, bases, attrs):
        print(name)
        if 'name' not in attrs:
            raise NotImplementedError("Must implement app.name")
        return super().__new__(cls, name, bases, attrs)



class AdminApp:
    models = []
    no_admin_models = []
    background_app = False
    sidebar = None

    # def __init__(self, name, link, **kwargs):
    #     self.name = name
    #     self.link = link
    #     self.short_description = kwargs.get('short_description')
    #     self.long_description = kwargs.get('long_description')
    #     self.icon = kwargs.get('icon')
    #     self.models = kwargs.get('models')
    #     self.version = kwargs.get('version')
  

    @property
    def name(self):
        raise NotImplementedError('Must implement module.name')

    @property
    def short_description(self):
        raise NotImplementedError('Must implement module.short_description')

    @property
    def long_description(self):
        raise NotImplementedError('Must implement module.long_description')

    @property
    def link(self):
        raise NotImplementedError('Must implement module.link')

    @property
    def icon(self):
        raise NotImplementedError('Must implement module.icon')


    @property
    def version(self):
        raise NotImplementedError('Must implement version')

    # module_name = 'admin'
    # module_icon = 'fa-home'
    # module_link = current_app.config['ADMIN']['HOME_URL']
    # module_short_description = 'Administration'
    # module_long_description = "Administration Dashboard and pages"
    # models = [AdminDashboard, AdminApp, User, Role]
    # version = '1.0'
    # sidebar = {
    #     'DASHBOARDS': [
    #         AdminDashboard, AdminApp
    #     ],
    #     'SYSTEM MODELS': [
    #         User, Role
    #     ]
    # }
