from flask import render_template, current_app, flash
from flask_login import current_user
from ez2erp import CONTEXT, db, APPS
from ez2erp.auth.permissions import check_read
from ez2erp.core.errors import PageError



class Breadcrumb:
    def __init__(self, title=None, parent=None, child=None):
        self.title = title
        self.parent = parent
        self.child = child


class Bookmark:
    def __init__(self, items):
        self.items = items


class BookmarkItem:
    def __init__(self, icon, link, title=""):
        self.icon = icon
        self.link = link
        self.title = title
        

class SidebarItem:
    def __init__(self, name, link=None, icon='box', **kwargs):
        self.name = name
        self.link = link
        self.icon = icon
        self.disabled = kwargs.get('disabled', False)
        
        if 'type' in kwargs:
            self.type = kwargs['type']
        else:
            self.type = 'single'

        if 'sub_items' in kwargs:
            self.sub_items = kwargs['sub_items']
        


# class Sidebar:
#     def __init__(self, **kwargs):
#         self.name = name
#         self.link = link
#         self.icon = icon
#         self.disabled = kwargs.get('disabled', False)
        
#         if 'type' in kwargs:
#             self.type = kwargs['type']
#         else:
#             self.type = 'single'

#         if 'sub_items' in kwargs:
#             self.sub_items = kwargs['sub_items']


#     @classmethod
#     def item(cls, name, link=None, icon='box', type=None, sub_items=None):
#         return cls(
#             name=name,
#             link=link,
#             icon=icon,
#             type=type,
#             sub_items=sub_items
#         )


# class Sidebar:
#     def __init__(self, items):
#         self.items = items


class PageConfig:
    def __init__(self, template=None, sidebar=None, **kwargs):
        self.template = template
        self.sidebar = sidebar


class Page:
    def __init__(self, config, model=None, **kwargs):
        self.config: PageConfig = config
        self.model = model
        self.params = kwargs
        self.columns = kwargs.get('columns')
        self.table_data = kwargs.get('table_data')
        self.with_actions = kwargs.get('with_actions', False)
        self.edit_function = kwargs.get('edit_function')
        self.create_function = kwargs.get('create_function')
        self.title = kwargs.get('title', 'ez2ERP')
        self.is_main = kwargs.get('is_main', False)
        self.form = kwargs.get('form')
        self.bookmark = kwargs.get('bookmark')

        self._setup_sidebar()
        self._setup_breadcrumb()
        # self._setup_bookmark()
        self._setup_form()
        
        
    def _setup_sidebar(self):
        if self.is_main:
            self._add_main_app_sidebar()

        if self.model and self.config.sidebar is None:
            self._add_main_app_sidebar()
        
        
    # def _setup_bookmark(self):
    #     if self.create_url:
    #         self.bookmark = Bookmark(items=[
                
    #         ])
    
    
    def  _setup_form(self):
        if 'form' in self.params:
            self.form = self.params.get('form')

    def _setup_breadcrumb(self):
        if 'breadcrumb' in self.params:
            self.breadcrumb = self.params['breadcrumb']
        else:
            if self.model:
                self.breadcrumb = Breadcrumb(
                    title="{}s".format(self.model.__name__),
                    parent='Admin',
                    child="{}s".format(self.model.__name__)
                )
            else:
                self.breadcrumb = Breadcrumb(
                    title='breadcrumb.title',
                    parent='breadcrumb.parent',
                    child='breadcrumb.child'
                )

    @classmethod
    def blank(cls, config, **kwargs):
        return cls(config, **kwargs)


    @classmethod
    def table(cls, model, columns, config=None, **kwargs):
        if config is None:
            config = PageConfig(
                template="admin/admin_wingo_table.html"
            )
        if config.template is None:
            config.template = "admin/admin_wingo_table.html"

        table_data = model.query.all(columns=columns)

        with_actions = kwargs.get('with_actions', False)
        edit_function = kwargs.get('edit_function')
        create_function = kwargs.get('create_function')
        
        # Add Actions column to the table
        if with_actions:
            columns, table_data = cls._add_actions_column(columns, table_data)
        
        bookmark = None
        if create_function:
            bookmark = Bookmark(items=[
                BookmarkItem(
                    icon='plus',
                    link=create_function,
                    title='Create New'
                )
            ])
        
        return cls(
            config, model, columns=columns, 
            table_data=table_data,
            with_actions=with_actions,
            edit_function=edit_function,
            create_function=create_function,
            bookmark=bookmark
        ).display()

        
    @classmethod
    def edit(cls, model, oid, form, config=None):
        if config is None:
            config = PageConfig(
                template="admin/form/admin_edit.html"
            )
        if config.template is None:
            config.template = "admin/form/admin_edit.html"

        obj = model.query.retrieve(oid)
        form.set_form_data(obj)
        return cls(config, model, form=form, obj=obj).display()


    @classmethod
    def create(cls, model, form, config=None):
        if config is None:
            config = PageConfig(
                template="admin/form/admin_create.html"
            )
        if config.template is None:
            config.template = "admin/form/admin_create.html"

        return cls(config, model, form=form).display()

    
    @staticmethod
    def _add_actions_column(columns, table_data):
        columns.append('Actions')
        for row in table_data:
            row.append('')
        return columns, table_data


    def display(self, **kwargs):
        context = {}
        if hasattr(self, 'columns'):
            context['columns'] = self.columns
        if hasattr(self, 'table_data'):
            context['table_data'] = self.table_data
        if hasattr(self, 'breadcrumb'):
            context['breadcrumb'] = self.breadcrumb
        if hasattr(self, 'with_actions'):
            context['with_actions'] = self.with_actions
        if hasattr(self, 'edit_function'):
            context['edit_function'] = self.edit_function
        if hasattr(self, 'create_function'):
            context['create_function'] = self.create_function
        if hasattr(self, 'form'):
            context['form'] = self.form
        if hasattr(self, 'bookmark'):
            context['bookmark'] = self.bookmark
    
        context['title'] = self.title
        context.update(kwargs)
        return render_template(self.config.template, sidebar=self.config.sidebar, **context)


    def _add_main_app_sidebar(self):
        for app in APPS:
            if current_app.config['ADMIN']['MAIN_APP'] == app.name:
                main_app = app
                break
        else:
            raise Exception("Please check the MAIN_APP in config.py")
        
        if self.config.sidebar:
            self.config.sidebar = self.config.sidebar + main_app.sidebar
        else:
            self.config.sidebar = main_app.sidebar


def notify(message, category):
    if category not in ['success', 'error']:
        raise Exception("ez2erp error: not valid notify.category")

    return flash(message, category)
