""" MODULE: ADMIN.ROUTES """
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from flask_cors import cross_origin
from sqlalchemy import text
from app import CONTEXT, db
from app.core.models import CoreModel, CoreModule
from app.admin import bp_admin
from app.auth.permissions import check_read



def admin_table(*models, fields, form=None, list_view_url='', create_url=None, create_button=False,\
    edit_url=None, extra_modal=None, kwargs=None, create_modal="admin/admin_create_modal.html",\
    view_modal="admin/admin_view_modal.html", action="admin/admin_actions.html",\
    template="admin/admin_table.html"):
    """
    Available kwargs:

    """

    model_name = models[0].__amname__
    table_name = models[0].__tablename__
    
    if not check_read(model_name):
        return render_template('auth/authorization_error.html',context=CONTEXT)


    query_module_name = CoreModel.query.filter_by(name=model_name).first()

    if query_module_name:
        check_module = CoreModule.query.get(query_module_name.module_id)
        CONTEXT['module'] = check_module.name

    CONTEXT['create_modal'] = {'title': model_name}
    CONTEXT['active'] = model_name
    CONTEXT['model'] = model_name
    
    if kwargs is not None:
        
        if 'model_data' in kwargs:
            model_data = kwargs.get('model_data')

        if 'template' in kwargs:
            template = kwargs.get('template')
        
        if 'active' in kwargs:
            CONTEXT['active'] = kwargs.get('active')
        
        if 'edit_url' in kwargs:
            edit_url = kwargs.get('edit_url')
        
        if 'create_url' in kwargs:
            create_url = kwargs.get('create_url')

        if 'module' in kwargs:
            CONTEXT['module'] = kwargs.get('module')

    if kwargs is None or 'model_data' not in kwargs:

        if len(models) == 1:
            model_data = models[0].query.with_entities(*fields).all()

        elif len(models) == 2:
            model_data = models[0].query.outerjoin(models[1]).with_entities(*fields).all()

        elif len(models) == 3:
            query1 = db.session.query(models[0],models[1],models[2])
            model_data = query1.outerjoin(models[1]).outerjoin(models[2]).with_entities(*fields).all()

    if form is not None:
        table_fields = form.index_headers
        title = form.title
        index_title = form.index_title
        index_message = form.index_message

        if view_modal or create_modal:
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
                        # TODO: Dapat rektang AdminField nalang iaappend sa fields hindi na dictionary
                        fields[row_count].append(
                            {
                                'name': field.name, 'label': field.label, 'type': field.input_type, 
                                'data': data,'placeholder':field.placeholder,'required':field.required,'readonly':field.readonly,
                                'auto_generated': field.auto_generated
                                })
                    else:
                        fields[row_count].append(
                            {
                                'name': field.name, 'label': field.label, 'type': field.input_type,
                                'placeholder':field.placeholder,'required':field.required,'readonly':field.readonly,
                                'auto_generated': field.auto_generated
                                })
                    field_count = field_count + 1
                    js_fields.append(field.name)
                if field_count <= 2:
                    field_sizes.append(6)
                elif field_count >= 3:
                    field_sizes.append(4)
                row_count = row_count + 1

            CONTEXT['create_modal'] = {
                'create_url': create_url,
                'fields_sizes':field_sizes,
                'js_fields':js_fields
            }

    else:
        if 'index_headers' not in kwargs:
            raise NotImplementedError('Must implement index_headers')
        else:
            table_fields = kwargs.get('index_headers')
        if 'index_title' not in kwargs:
            raise NotImplementedError("Must implement index_title")
        else:
            index_title = kwargs.get('index_title')
            title = index_title
        if 'index_message' not in kwargs:
            raise NotImplementedError("Must implement index_message")
        else:
            index_message = kwargs.get('index_message')
    
    CONTEXT['current_list_view_url'] = list_view_url

    print(model_data)
    return render_template(template, context=CONTEXT, form=form, create_fields=fields, create_button=create_button,
                        model_data=model_data, table_fields=table_fields,
                        heading=index_title, sub_heading=index_message,
                        title=title, action=action, create_modal=create_modal, extra_modal=extra_modal,
                        view_modal=view_modal, edit_url=edit_url,table=table_name,rendered_model=models[0])


def admin_edit(form, update_url, oid, modal_form=False, action="admin/admin_edit_actions.html", \
    model=None,extra_modal=None, scripts=None, template="admin/admin_edit.html", kwargs=None):
    fields = []
    row_count = 0
    field_sizes = []

    for row in form.edit_fields():
        fields.append([])
        field_count = 0

        for field in row:

            if field.input_type == 'select':
                data = field.model.query.all()
                # TODO: Dapat rektang AdminField nalang iaappend sa fields hindi na dictionary
                fields[row_count].append(
                    {'name': field.name, 'label': field.label, 'type': field.input_type, 'data': data,
                     'value': field.data,'placeholder':field.placeholder,'required':field.required})
            else:
                fields[row_count].append({'name': field.name, 'label': field.label, 'type': field.input_type,
                                          'value': field.data,'placeholder':field.placeholder,'required':field.required,
                                          'readonly': field.readonly
                                          })
            field_count = field_count + 1

        if field_count <= 2:
            field_sizes.append(6)
        elif field_count >= 3:
            field_sizes.append(4)

        row_count = row_count + 1

    CONTEXT['edit_model'] = {
        'fields_sizes':field_sizes,
    }

    if model:
        model_name = model.__amname__
        CONTEXT['create_modal']['title'] = model_name
        CONTEXT['active'] = model_name
        delete_table = model.__tablename__

    query1 = CoreModel.query.filter_by(name=model_name).first()

    if query1:
        check_module = CoreModule.query.get(query1.module_id)
        CONTEXT['module'] = check_module.name

    if kwargs is not None:
        if 'template' in kwargs:
            template = kwargs.get('template')

        if 'active' in kwargs:
            CONTEXT['active'] = kwargs.get('active')
        
        if 'update_url' in kwargs:
            update_url = kwargs.get('update_url')
    
    return render_template(template, context=CONTEXT, form=form, update_url=update_url, edit_fields=fields,
                           oid=oid,modal_form=modal_form,edit_title=form.edit_title,delete_table=delete_table, scripts=scripts,
                           action=action,extra_modal=extra_modal, title=form.edit_title,rendered_model=model)


def admin_dashboard(box1=None,box2=None,box3=None,box4=None):
    from app.auth.models import User
    if not box1:
        box1 = DashboardBox("Total Modules","Installed",CoreModule.query.count())

    if not box2:
        box2 = DashboardBox("System Models","Total models",CoreModel.query.count())

    if not box3:
        box3 = DashboardBox("Users","Total users",User.query.count())
    
    CONTEXT['active'] = 'main_dashboard'
    CONTEXT['module'] = 'admin'

    return render_template("admin/admin_dashboard.html", context=CONTEXT,title='Admin Dashboard', \
        box1=box1,box2=box2,box3=box3)


@bp_admin.route('/') # move to views
@login_required
def dashboard():
    return admin_dashboard()


@bp_admin.route('/apps')
def apps():
    CONTEXT['active'] = 'apps'
    modules = CoreModule.query.all()
    return render_template('admin/admin_apps.html',context=CONTEXT,title='Apps',modules=modules)


@bp_admin.route('/delete/<string:delete_table>/<int:oid>',methods=['POST'])
@login_required
def delete(delete_table,oid):
    try:
        index_url = request.args.get('index_url')
        query = "DELETE from {} where id = {}".format(delete_table,oid)
        db.engine.execute(text(query))
        flash('Deleted Successfully!','success')
        return redirect(url_for(index_url))
    except Exception as e:
        flash(str(e),'error')
        return redirect(request.referrer)


@bp_admin.route('/delete-data',methods=["POST"])
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
        res = [x[0] if x[0] is not None else '' for x in row]
        resp = jsonify(result=str(res[0]),column=column)
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify(result="")
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.status_code = 200
        return resp


class DashboardBox:
    def __init__(self,heading,subheading, number):
        self.heading = heading
        self.subheading = subheading
        self.number = number