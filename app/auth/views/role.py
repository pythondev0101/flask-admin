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
    form.inline.data = CoreModel.query.all()

    return admin_table(Role, fields=fields, form=form, create_modal_template="auth/role_create_modal.html", \
        create_url='bp_auth.create_role',edit_url='bp_auth.edit_role', \
            view_modal_template="auth/role_view_modal.html", **options)


@bp_auth.route('/roles/create',methods=['GET','POST'])
@login_required
def create_role():
    form = RoleCreateForm()

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


@bp_auth.route('/roles/<int:oid>/edit',methods=['GET','POST'])
@login_required
def edit_role(oid,**options):
    role = Role.query.get_or_404(oid)
    form = RoleEditForm(obj=role)

    if request.method == "GET":
        role_permissions = RolePermission.query.filter_by(role_id=oid).all()
        form.permission_inline.data = role_permissions
        
        _scripts = [
            {'bp_auth.static': 'js/role.js'},
            {'bp_admin.static': 'js/admin_edit.js'}
        ]

        return admin_edit(Role, form, "bp_auth.edit_role", oid, 'bp_auth.roles', scripts=_scripts, \
            **options)

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


@bp_auth.route('/roles/<int:oid1>/permissions/<int:oid2>/edit', methods=['POST'])
@cross_origin()
def role_edit_permission(oid1, oid2):
    
    permission_type = request.json['permission_type']
    value = request.json['value']

    permission = RolePermission.query.get_or_404(oid2)

    if not permission:
        resp = jsonify(0)
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.status_code = 200

        return resp

    if permission_type == 'read':
        permission.read = value
    
    elif permission_type == 'create':
        permission.create = value

    elif permission_type == 'write':
        permission.write = value
    
    elif permission_type == "delete":
        permission.delete = value

    db.session.commit()
    
    load_permissions(current_user.id)

    resp = jsonify(1)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.status_code = 200

    return resp
