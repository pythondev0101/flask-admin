""" MODULE: ADMIN.ROUTES """
""" FLASK IMPORTS """
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import login_required

"""--------------END--------------"""

""" APP IMPORTS  """
from app import system_modules
from app.admin import bp_admin

"""--------------END--------------"""

""" TEMPLATES IMPORTS """
from . import admin_templates

"""--------------END--------------"""
from . import context


@bp_admin.route('/')
@login_required
def index():
    # TODO: return total tables,users...
    context['title'] = 'Admin'
    context['active'] = 'main_dashboard'
    return render_template(admin_templates['index'], context=context)


def admin_edit(form, fields_data, update_url, oid, modal_form=False, template="admin/admin_edit.html"):
    # Note: fields_data is just temporary
    # TODO: inherit flask form to get values in constructor
    fields = []
    row_count = 0
    field_count = 0
    for row in form.edit_fields:
        fields.append([])
        for field in row:
            if field.input_type == 'select':
                data = field.data.query.all()
                fields[row_count].append(
                    {'name': field.name, 'label': field.label, 'type': field.input_type, 'data': data,
                     'value': fields_data[field_count]})
            else:
                fields[row_count].append({'name': field.name, 'label': field.label, 'type': field.input_type,
                                          'value': fields_data[field_count]})
            field_count = field_count + 1
        row_count = row_count + 1
    context['edit_model'] = {
        'fields': fields
    }

    return render_template(template, context=context, form=form, update_url=update_url,
                           oid=oid,modal_form=modal_form,edit_title=form.edit_title,)


def admin_index(*model, fields, url, form, action="admin/admin_actions.html",
                create_modal="admin/admin_create_modal.html", view_modal="admin/admin_view_modal.html",
                create_url="", edit_url="", template="admin/admin_index.html", active=""):
    page = request.args.get('page', 1, type=int)
    data_per_page = current_app.config['DATA_PER_PAGE']
    if len(model) == 1:
        models = model[0].query.with_entities(*fields).paginate(page, data_per_page, False)
        print(model[0].query.with_entities(*fields))
    else:
        models = model[0].query.outerjoin(model[1]).with_entities(*fields).paginate(page, data_per_page, False)
        print(model[0].query.outerjoin(model[1]).with_entities(*fields))

    table_fields = form.index_headers
    title = form.title
    index_title = form.index_title
    index_message = form.index_message

    next_url = url_for(url, page=models.next_num) \
        if models.has_next else None
    prev_url = url_for(url, page=models.prev_num) \
        if models.has_prev else None

    context['create_modal']['title'] = model[0].model_name
    context['active'] = model[0].model_name
    if active:
        context['active'] = active

    if create_url and create_modal:
        set_modal(create_url, form)

    return render_template(template, context=context,
                           models=models.items, table_fields=table_fields,
                           next_url=next_url, prev_url=prev_url,
                           index_title=index_title, index_message=index_message,
                           title=title, action=action, create_modal=create_modal,
                           view_modal=view_modal, edit_url=edit_url)


def set_modal(url, form):
    fields = []
    row_count = 0
    for row in form.create_fields:
        fields.append([])
        for field in row:
            if field.input_type == 'select':
                data = field.data.query.all()
                fields[row_count].append(
                    {'name': field.name, 'label': field.label, 'type': field.input_type, 'data': data})
            else:
                fields[row_count].append({'name': field.name, 'label': field.label, 'type': field.input_type})
        row_count = row_count + 1
    context['create_modal'] = {
        'create_url': url,
        'create_form': form,
        'fields': fields
    }
