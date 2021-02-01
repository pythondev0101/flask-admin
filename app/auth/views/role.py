from datetime import datetime
from flask import flash, redirect, url_for, request, jsonify
from flask_cors import cross_origin
from flask_login import current_user, login_required
from app.auth import bp_auth
from app import db
from app.auth.models import Role, RolePermission
from app.auth.forms import RoleCreateForm, RoleEditForm
from app.core.models import CoreModel
from app.admin.templating import admin_table, admin_edit
from app.auth.permissions import load_permissions



@bp_auth.route('/roles')
@login_required
def roles(**options):
    fields = [Role.id,Role.name,Role.created_at, Role.updated_at]
    form = RoleCreateForm()
    form.inline.models = CoreModel.query.all()

    return admin_table(Role, fields=fields, form=form, create_modal_template="auth/role_create_modal.html", \
        create_url='bp_auth.role_create',edit_url='bp_auth.role_edit', \
            view_modal_template="auth/role_view_modal.html", **options)


@bp_auth.route('/role_create',methods=['GET','POST'])
@login_required
def role_create():
    form = RoleCreateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            role = Role()
            role.name = form.name.data
            models = CoreModel.query.all()
            r = request.form
            for model in models:
                mid = model.id
                has_model = False
                read,create,write,delete = 0,0,0,0
                read_string = 'chk_read_{}'.format(mid)
                create_string = 'chk_create_{}'.format(mid)
                write_string = 'chk_write_{}'.format(mid)
                delete_string = 'chk_delete_{}'.format(mid)

                if r.get(read_string) == 'on': read,has_model = 1,True
                if r.get(create_string) == 'on': create,has_model = 1,True
                if r.get(write_string) == 'on': write,has_model = 1, True
                if r.get(delete_string) == 'on': delete,has_model = 1,True

                if has_model:
                    permission = RolePermission(model=model,read=read,create=create,write=write,delete=delete)
                    role.role_permissions.append(permission)
            
            db.session.add(role)
            db.session.commit()
            flash('Role added successfully!','success')
            return redirect(url_for('bp_auth.roles'))


@bp_auth.route('/role_edit/<int:oid>',methods=['GET','POST'])
@login_required
def role_edit(oid,**options):
    role = Role.query.get_or_404(oid)
    form = RoleEditForm(obj=role)

    if request.method == "GET":
        role_permissions = RolePermission.query.filter_by(role_id=oid).all()
        query1 = db.session.query(RolePermission.model_id).filter_by(role_id=oid)
        models = db.session.query(CoreModel).filter(~CoreModel.id.in_(query1))
        form.model_inline.models = models
        form.permission_inline.models = role_permissions
        
        return admin_edit(Role, form, "bp_auth.role_edit", oid, 'bp_auth.roles', **options)

    if not form.validate_on_submit():
        for key, value in form.errors.items():
            flash(str(key) + str(value), 'error')
        return redirect(url_for('bp_auth.roles'))

    try:
        role.name = form.name.data
        role.updated_at = datetime.now()
        db.session.commit()
        flash('Role update Successfully!','success')
    except Exception as e:
        flash(str(e),'error')

    return redirect(url_for('bp_auth.roles'))


@bp_auth.route('/role_add_permission/<int:oid>/', methods=['POST'])
@login_required
def role_add_permission(oid):
    if request.method == "POST":
        role = Role.query.get_or_404(oid)
        model = CoreModel.query.filter_by(id=request.args.get('model_id')).first()
        read, create, write, delete = request.form.get('chk_read', 0), request.form.get('chk_create', 0), \
            request.form.get('chk_write', 0), request.form.get('chk_delete', 0)
        if read == 'on': read = 1
        if create == 'on': create = 1
        if write == 'on': write = 1
        if delete == 'on': delete = 1
        permission = RolePermission(role_id=role.id, model=model, read=read, create=create, write=write, delete=delete)
        role.role_permissions.append(permission)
        db.session.commit()
        load_permissions(current_user.id)
        return redirect(url_for('bp_auth.role_edit', oid=oid))


@bp_auth.route('/role_delete_permission/<int:oid>/', methods=['POST'])
@login_required
def role_delete_permission(oid):
    if request.method == "POST":
        try:
            permission = RolePermission.query.get(oid)
            db.session.delete(permission)
            db.session.commit()
            load_permissions(current_user.id)
            return redirect(request.referrer)
        except Exception as e:
            db.session.rollback()
            flash("Error occured: " + str(e),'error')
            return redirect(request.referrer)

@bp_auth.route('/role_edit_permission', methods=['POST'])
@cross_origin()
def role_edit_permission():
    if request.method == 'POST':
        permission_id = request.json['permission_id']
        read = request.json['read']
        create = request.json['create']
        write = request.json['write']
        delete = request.json['delete']
        permission = RolePermission.query.get(permission_id)
        if permission:
            permission.read = read
            permission.create = create
            permission.write = write
            permission.delete = delete
            db.session.commit()
            load_permissions(current_user.id)
            resp = jsonify(1)
            resp.headers.add('Access-Control-Allow-Origin', '*')
            resp.status_code = 200
            return resp
        else:
            resp = jsonify(0)
            resp.headers.add('Access-Control-Allow-Origin', '*')
            resp.status_code = 200
            return resp