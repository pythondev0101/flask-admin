""" MODULE: ADMIN.ROUTES """
""" FLASK IMPORTS """
from flask import render_template, flash, redirect, url_for, request, current_app,g,jsonify
from flask_login import login_required
"""--------------END--------------"""

""" APP IMPORTS  """
from app.admin import bp_admin

"""--------------END--------------"""

""" TEMPLATES IMPORTS """
from . import admin_templates
"""--------------END--------------"""

from app import context
from app.core.models import HomeBestModel
from sqlalchemy import text
from flask_cors import cross_origin
from app import db

@bp_admin.route('/')
@login_required
def dashboard():
    return admin_dashboard()

    

@bp_admin.route('/_delete_data',methods=["POST"])
@cross_origin()
def delete_data():
    table = request.json['table']
    data = request.json['ids']
    try:
        if not data:
            resp = jsonify(result=2)
            resp.headers.add('Access-Control-Allow-Origin', '*')
            resp.status_code = 200
            return resp

        for idx in data:
            query = "DELETE from {} where id = {}".format(table,idx)
            db.engine.execute(text(query))

        resp = jsonify(result=1)
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.status_code = 200
        flash('Successfully deleted!','success')
        return resp
    except Exception as e:
        flash(str(e),'error')
        db.session.rollback()
        resp = jsonify(result=0)
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.status_code = 200
        return resp
    

@bp_admin.route('/_get_view_modal_data',methods=["POST"])
@cross_origin()
def get_view_modal_data():
    try:
        table,column,id = request.json['table'],request.json['column'],request.json['id']
        query = "select {} from {} where id = {} limit 1".format(column,table,id)
        sql = text(query)
        row = db.engine.execute(sql)
        res = [x[0] for x in row]
        resp = jsonify(result=res[0],column=column)
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify(result="")
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.status_code = 200
        return resp


def admin_edit(form, update_url, oid, modal_form=False, action=None, \
    model=None,extra_modal=None , template="admin/admin_edit.html"):
    # TODO: inherit flask form to get values in constructor
    fields = []
    row_count = 0
    
    for row in form.edit_fields():
        fields.append([])
        for field in row:
            if field.input_type == 'select':
                data = field.model.query.all()
                fields[row_count].append(
                    {'name': field.name, 'label': field.label, 'type': field.input_type, 'data': data,
                     'value': field.data})
            else:
                fields[row_count].append({'name': field.name, 'label': field.label, 'type': field.input_type,
                                          'value': field.data})
        row_count = row_count + 1
    context['edit_model'] = {
        'fields': fields
    }

    if model:
        model_name = model.model_name
        context['create_modal']['title'] = model_name
        context['active'] = model_name
        check_module = HomeBestModel.query.with_entities(HomeBestModel.module).filter_by(name=model_name).first()
        if check_module:
            context['module'] = check_module[0]


    return render_template(template, context=context, form=form, update_url=update_url,
                           oid=oid,modal_form=modal_form,edit_title=form.edit_title,action=action,extra_modal=extra_modal)


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

    model_name = model[0].model_name
    context['create_modal']['title'] = model_name
    context['active'] = model_name
    check_module = HomeBestModel.query.with_entities(HomeBestModel.module).filter_by(name=model_name).first()
    if check_module:
        context['module'] = check_module[0]
    if active:
        context['active'] = active

    if create_url and create_modal:
        set_modal(create_url, form)

    table = model[0].__tablename__

    return render_template(template, context=context,
                           models=models.items, table_fields=table_fields,
                           next_url=next_url, prev_url=prev_url,
                           index_title=index_title, index_message=index_message,
                           title=title, action=action, create_modal=create_modal,
                           view_modal=view_modal, edit_url=edit_url,table=table)


def set_modal(url, form):
    fields = []
    row_count = 0
    field_sizes = []
    js_fields = []
    for row in form.create_fields():
        fields.append([])
        field_count = 0
        for field in row:
            if field.input_type == 'select':
                data = field.model.query.all()
                fields[row_count].append(
                    {'name': field.name, 'label': field.label, 'type': field.input_type, 'data': data,'placeholder':field.placeholder})
            else:
                fields[row_count].append({'name': field.name, 'label': field.label, 'type': field.input_type,'placeholder':field.placeholder})
            field_count = field_count + 1
            js_fields.append(field.name)
        if field_count <= 2:
            field_sizes.append(6)
        elif field_count >= 3:
            field_sizes.append(4)
        row_count = row_count + 1
    context['create_modal'] = {
        'create_url': url,
        'create_form': form,
        'fields': fields,
        'fields_sizes':field_sizes,
        'js_fields':js_fields
    }


def admin_dashboard(box1=None,box2=None,box3=None,box4=None):
    from app.auth.models import User
    if not box1:
        box1 = DashboardBox("Total Modules","Installed",db.session.query(HomeBestModel.module).count())

    if not box2:
        box2 = DashboardBox("System Models","Total models",HomeBestModel.query.count())

    if not box3:
        box3 = DashboardBox("Users","Total users",User.query.count())
    
    context['active'] = 'main_dashboard'
    context['module'] = 'admin'
    return render_template("admin/admin_dashboard.html", context=context,title='Admin Dashboard', \
        box1=box1,box2=box2,box3=box3)


class DashboardBox:
    def __init__(self,heading,subheading, number):
        self.heading = heading
        self.subheading = subheading
        self.number = number