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


def change_context(view):
    # VALUES: title, module, active, forms, modal
    context['module'] = 'admin'
    if view == 'index':
        context['title'] = 'Admin'
        context['active'] = 'main_dashboard'
        context['modal'] = False


@bp_admin.route('/')
@login_required
def index():
    # TODO: return total tables,users...
    change_context('index')
    return render_template(admin_templates['index'], context=context)


def admin_index(*model, fields, admin_index_url, admin_index_template="admin/admin_index.html"):
    page = request.args.get('page', 1, type=int)
    data_per_page = current_app.config['DATA_PER_PAGE']
    print(len(model))
    if len(model) == 1:
        models = model[0].query.with_entities(*fields).paginate(page, data_per_page, False)
    else:
        models = model[0].query.join(model[1]).with_entities(*fields).paginate(page, data_per_page, False)

    table_fields = model[0].index_fields
    context['active'] = model[0].model_name
    title = model[0].title
    index_title = model[0].index_title
    index_message = model[0].index_message
    next_url = url_for(admin_index_url, page=models.next_num) \
        if models.has_next else None
    prev_url = url_for(admin_index_url, page=models.prev_num) \
        if models.has_prev else None
    context['modal'] = True
    return render_template(admin_index_template, context=context,
                           models=models.items, table_fields=table_fields,
                           next_url=next_url, prev_url=prev_url,
                           index_title=index_title,index_message=index_message,
                           title=title)
