class PageConfig(object):
    sidebar_html = "admin/sidebar.html"
    
    def __init__(self, **kwargs):
        if 'sidebar_html' in kwargs:
            self.sidebar_html = kwargs['sidebar_html']
            

class Page(object):
    config: PageConfig
    
    def __init__(self, page_config):
        self.config = page_config
