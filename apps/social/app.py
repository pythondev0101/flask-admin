from ez2erp.admin import AdminApp



class Social(AdminApp):
    name = 'social'
    icon = 'fa-home'
    link = 'bp_admin.dashboard'
    short_description = 'Social'
    long_description = """
        An application that allows people to share information or to bring people together
    """
    version = 1.0
