from flask import render_template
from sqlalchemy.sql.expression import table
from app import MODULES, CONTEXT, db
from app.core.models import CoreModel, CoreModule
from app.auth.permissions import check_read



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
    from app.auth.models import User

    options = {
        'dashboard_template': "admin/admin_dashboard.html",
        'box1': None,'box2': None,'box3': None,'box4': None,
        'data': None,
        'title': 'Admin Dashboard',
        'module': 'admin',
    }

    options.update(kwargs)

    active_model = model.__amname__
    
    return admin_render_template(model, options['dashboard_template'], options['module'], title=options['title'], \
        options=options, data=options['data'], active_model=active_model)


def admin_table(*models, fields, form=None, **options):
 
    model_name = models[0].__amname__
    table_name = models[0].__tablename__

    if not check_read(model_name):
        return render_template('auth/authorization_error.html',context=CONTEXT)

    table_options = {
        'module_name': None,
        'table_template': "admin/admin_table.html",
        'create_modal_template': "admin/admin_create_modal.html",
        'view_modal_template': "admin/admin_view_modal.html",
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
        'create_modal': None, # Form is needed to enable
        'view_modal': None, # Form is needed
        'parent_model': None,
        'table_name': table_name,
        'modals': [],
        'scripts': [
            {'bp_admin.static': 'js/admin_table.js'}
            ]
    }

    table_options.update(options)

    if table_options['module_name'] is None:
        _query_module_name = CoreModel.query.filter_by(name=model_name).first()
        table_options['module_name'] = CoreModule.query.get(_query_module_name.module_id).name
    
    if models[0].__parent_model__ is not None:
        table_options['parent_model'] = models[0].__parent_model__
    
    if table_options['table_data'] is None:
        if len(models) == 1:
            table_options['table_data'] = models[0].query.with_entities(*fields).all()

        elif len(models) == 2:
            table_options['table_data'] = models[0].query.outerjoin(models[1]).with_entities(*fields).all()

        elif len(models) == 3:
            _query1 = db.session.query(models[0],models[1],models[2])
            table_options['table_data'] = _query1.outerjoin(models[1]).outerjoin(models[2]).with_entities(*fields).all()
    
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

        if table_options['view_modal'] is None: # Kung wala, iseset nya sa true dahil may form naman
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

    return admin_render_template(models[0], table_options['table_template'], table_options['module_name'],\
        FORM=form, TABLE_OPTIONS=table_options, MODAL_DATA=modal_data, scripts=table_options['scripts'], \
            modals=table_options['modals'], title=table_options['title'])


def admin_edit(model, form, update_url, oid, table_url, **options):
    
    model_name = model.__amname__
    _query1 = CoreModel.query.filter_by(name=model_name).first()
    module_name = CoreModule.query.get(_query1.module_id).name

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

    return admin_render_template(model, edit_options['edit_template'], edit_options['module_name'], FORM=form,\
        EDIT_OPTIONS=edit_options, OID=oid, scripts=edit_options['scripts'], modals=edit_options['modals'],\
            title=edit_options['title'])


class DashboardBox:
    def __init__(self,heading,subheading, number):
        self.heading = heading
        self.subheading = subheading
        self.number = number
