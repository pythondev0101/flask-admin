from flask import render_template
from flask_login import current_user
from ez2erp import CONTEXT, db
# from ez2erp.core.models import CoreModel, CoreModule
from ez2erp.auth.permissions import check_read
from ez2erp.core.errors import PageError



class Breadcrumb:
    def __init__(self, title=None, parent=None, child=None):
        self.title = title
        self.parent = parent
        self.child = child


class SidebarItem:
    def __init__(self, name, link=None, icon='home', **kwargs):
        self.name = name
        self.link = link
        self.icon = icon
        if 'type' in kwargs:
            self.type = kwargs['type']
        else:
            self.type = 'single'

        if 'sub_items' in kwargs:
            self.sub_items = kwargs['sub_items']


class Sidebar:
    def __init__(self, items):
        self.items = items


class PageConfig:
    def __init__(self, template=None, sidebar=None, **kwargs):
        self.template = template
        self.sidebar = sidebar


class Page:
    def __init__(self, config, model=None, **kwargs):
        self.config: PageConfig = config
        self.model = model
        self.columns = kwargs.get('columns')
        self.table_data = kwargs.get('table_data')
        self.with_actions = kwargs.get('with_actions', False)
        self.edit_url = kwargs.get('edit_url')
        self.title = kwargs.get('title', 'ez2ERP')

        if 'breadcrumb' in kwargs:
            self.breadcrumb = kwargs['breadcrumb']
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

        if 'form' in kwargs:
            self.form = kwargs.get('form')


    @classmethod
    def blank(cls, config, **kwargs):
        return cls(config, **kwargs)


    @classmethod
    def table(cls, model, columns, config=None, **kwargs):
        if config is None:
            config = PageConfig(
                template="admin/admin_wingo_table.html", 
                sidebar=[],
            )
        if config.template is None:
            config.template = "admin/admin_wingo_table.html"

        table_data = model.query.all(columns=columns)
        print("table_data:", table_data)
        # Add Actions column to the table
        with_actions = kwargs.get('with_actions', False)
        if with_actions:
            columns, table_data = cls._add_actions_column(columns, table_data)
            
        edit_url = kwargs.get('edit_url')
        return cls(
            config, model, columns=columns, 
            table_data=table_data,
            with_actions=with_actions,
            edit_url=edit_url
        )

        
    @classmethod
    def edit(cls, model, oid, form=None, config=None):
        if config is None:
            config = PageConfig(
                template="admin/admin_wingo_edit.html",
                sidebar=[]
            )
        if config.template is None:
            config.template = "admin/admin_wingo_edit.html"

        obj = model.query.retrieve(oid)
        form.set_form_data(obj)
        return cls(config, model, form=form, obj=obj)

    
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
        if hasattr(self, 'edit_url'):
            context['edit_url'] = self.edit_url
        if hasattr(self, 'form'):
            context['form'] = self.form
        
        context['title'] = self.title
        context.update(kwargs)
        return render_template(self.config.template, sidebar=self.config.sidebar, **context)


# def display_normal_page(page):
#     template = page.template
#     return render_template(template, sidebar=sidebar)


def admin_render_template(rendered_model, template_name_or_list, module_name, scripts=None, modals=None, **context):
    vdata = {
        'sidebar': None,
        'module': None,
    }

    module = None

    for _module in MODULES:
        if _module.module_name == module_name:
            module = _module
            vdata['module'] = _module
            break

    if module is not None and module.sidebar is not None:
        vdata['sidebar'] = module.sidebar

    context['VDATA'] = vdata
    context['SCRIPTS'] = scripts
    context['MODALS'] = modals
    context['CONTEXT'] = CONTEXT
    context['MODULES'] = MODULES
    context['RENDERED_MODEL'] = rendered_model

    return render_template(template_name_or_list, **context)


def admin_dashboard(model, **kwargs):
    options = {
        'dashboard_template': "admin/admin_wingo_dashboard.html",
        'box1': None, 'box2': None, 'box3': None, 'box4': None,
        'data': None,
        'title': 'Admin Dashboard',
        'module': 'admin',
    }

    options.update(kwargs)

    active_model = model.__amname__

    return admin_render_template(model, options['dashboard_template'], options['module'], title=options['title'],
                                 options=options, data=options['data'], active_model=active_model, UID=str(current_user.id))


def admin_table(*models, fields, form=None, **options):
    if 'table_data' not in options:
        raise NotImplementedError('Must implement table_data')

    model_name = models[0].__amname__
    table_name = models[0].__tablename__

    if not check_read(model_name):
        return render_template('auth/authorization_error.html', context=CONTEXT)

    table_options = {
        'module_name': None,
        'table_template': "admin/admin_table.html",
        'create_modal_template': "admin/admin_create_modal.html",
        'view_modal_template': "admin/admin_view_modal.html",
        'view_modal_url': None,
        'action_template': "admin/admin_actions.html",
        'table_data': None,
        'table_url': None,
        'table_columns': None,
        'heading': model_name + "s Table",
        'subheading': None,
        'title': model_name + "s Table",
        'create_url': None,
        'edit_url': None,
        'create_button': False,
        'actions': True,
        'create_modal': None,  # Form is needed to enable
        'view_modal': None,  # Form is needed
        'parent_model': None,
        'table_name': table_name,
        'modals': [],
        'scripts': [
            {'bp_admin.static': 'js/admin_table.js'}
        ]
    }

    table_options.update(options)

    if table_options['module_name'] is None:
        _query_module_name = CoreModel.objects(name=model_name).first()
        table_options['module_name'] = CoreModule.objects.get(
            id=_query_module_name.module.id).name

    if models[0].__parent_model__ is not None:
        table_options['parent_model'] = models[0].__parent_model__

    if table_options['table_data'] is None:
        if len(models) == 1:
            table_options['table_data'] = models[0].objects.scalar(*fields)

        elif len(models) == 2:
            table_options['table_data'] = models[0].query.outerjoin(
                models[1]).with_entities(*fields).all()

        elif len(models) == 3:
            _query1 = db.session.query(models[0], models[1], models[2])
            table_options['table_data'] = _query1.outerjoin(
                models[1]).outerjoin(models[2]).with_entities(*fields).all()

    modal_data = {
        'create_url': None,
        'fields_sizes': None,
        'js_fields': None,
        'title': None,
    }

    if form:
        table_options['table_columns'] = form.__table_columns__
        table_options['title'] = form.__title__
        table_options['heading'] = form.__heading__
        table_options['subheading'] = form.__subheading__

        # Kung wala, iseset nya sa true dahil may form naman
        if table_options['view_modal'] is None:
            table_options['view_modal'] = True

        if table_options['create_modal'] is None:
            table_options['create_modal'] = True

        if table_options['view_modal'] or table_options['create_modal']:
            _row_count = 0
            _field_sizes = []
            _js_fields = []

            for row in form.fields:
                _field_count = 0

                for field in row:
                    _field_count = _field_count + 1
                    _js_fields.append(field.name)

                if _field_count <= 2:
                    _field_sizes.append(6)
                elif _field_count >= 3:
                    _field_sizes.append(4)
                _row_count = _row_count + 1

            modal_data['create_url'] = table_options['create_url']
            modal_data['fields_sizes'] = _field_sizes
            modal_data['js_fields'] = _js_fields
            modal_data['title'] = model_name

    return admin_render_template(models[0], table_options['table_template'], table_options['module_name'],
                                 FORM=form, TABLE_OPTIONS=table_options, MODAL_DATA=modal_data, scripts=table_options[
                                     'scripts'],
                                 modals=table_options['modals'], title=table_options['title'])


def admin_edit(model, form, update_url, oid, table_url, **options):

    model_name = model.__amname__
    _query1 = CoreModel.objects(name=model_name).first()
    module_name = CoreModule.objects.get(id=_query1.module.id).name

    edit_options = {
        'module_name': module_name,
        'update_url': update_url,
        'edit_template': "admin/admin_edit.html",
        'action_template': "admin/admin_edit_actions.html",
        'actions': True,
        'table_name': model.__tablename__,
        'scripts': [
            {'bp_admin.static': 'js/admin_edit.js'}
        ],
        'modals': [],
        'title': form.__title__,
        'heading': form.__heading__,
        'subheading': form.__subheading__,
        'parent_model': None,
        'table_url': table_url,
        'fields_sizes': [],
    }

    edit_options.update(options)

    if model.__parent_model__ is not None:
        edit_options['parent_model'] = model.__parent_model__

    for row in form.fields:
        _field_count = 0

        for field in row:
            _field_count = _field_count + 1

        if _field_count <= 2:
            edit_options['fields_sizes'].append(6)
        elif _field_count >= 3:
            edit_options['fields_sizes'].append(4)

    return admin_render_template(model, edit_options['edit_template'], edit_options['module_name'], FORM=form,
                                 EDIT_OPTIONS=edit_options, OID=oid, scripts=edit_options[
                                     'scripts'], modals=edit_options['modals'],
                                 title=edit_options['title'])


class DashboardBox:
    def __init__(self, heading, subheading, number):
        self.heading = heading
        self.subheading = subheading
        self.number = number
