from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_required
from flask_cors import cross_origin
from app import db
from app.core.models import CoreModel
from app.core.logging import create_log
from app.auth import bp_auth
from app.auth.models import User, UserPermission
from app.auth.forms import UserForm, UserEditForm, UserPermissionForm
from app.auth import auth_urls
from app.auth.permissions import load_permissions, check_create
from app.admin.routes import admin_table, admin_edit



@bp_auth.route('/permissions')
@login_required
def user_permission_index():
    fields = [UserPermission.id, User.username, User.fname, CoreModel.name, UserPermission.read, UserPermission.create,
              UserPermission.write, UserPermission.delete]
    model = [UserPermission, User,CoreModel]
    form = UserPermissionForm()
    return admin_table(*model, fields=fields, form=form, url=auth_urls['user_permission_index'], create_modal=False,
                       view_modal=False, active="Users")


@bp_auth.route('/users')
@login_required
def users(**kwargs):
    form = UserForm()
    fields = [User.id, User.username, User.fname, User.lname, User.email]
    models = [User]
    return admin_table(*models, fields=fields, url=auth_urls['index'], create_url='bp_auth.user_create', edit_url="bp_auth.user_edit", form=form,kwargs=kwargs)


@bp_auth.route('/username_check', methods=['POST'])
def username_check():
    if request.method == 'POST':
        username = request.json['username']
        user = User.query.filter_by(username=username).first()
        if user:
            resp = jsonify(result=0)
            resp.status_code = 200
            return resp
        else:
            resp = jsonify(result=1)
            resp.status_code = 200
            return resp


@bp_auth.route('/_email_check',methods=["POST"])
def email_check():
    if request.method == 'POST':
        email = request.json['email']
        user = User.query.filter_by(email=email).first()
        if user:
            resp = jsonify(result=0)
            resp.status_code = 200
            return resp
        else:
            resp = jsonify(result=1)
            resp.status_code = 200
            return resp


@bp_auth.route('/change_password/<int:oid>',methods=['POST'])
def change_password(oid):
    user = User.query.get_or_404(oid)
    user.set_password(request.form.get('password'))
    db.session.commit()
    flash("Password change successfully!",'success')
    return redirect(request.referrer)


@bp_auth.route('/user_create', methods=['POST'])
@login_required
def user_create(**kwargs):
    if check_create('Users'):
        url = auth_urls['index']
        if 'url' in kwargs:
            url = kwargs.get('url')
        try:
            form = UserForm()
            if request.method == "POST":
                if form.validate_on_submit():
                    user = User()
                    models = CoreModel.query.all()
                    for model in models:
                        permission = UserPermission(model=model, read=1,create=0, write=0, delete=0)
                        user.permissions.append(permission)
                    user.username = form.username.data
                    user.fname = form.fname.data
                    user.lname = form.lname.data
                    if form.email.data == '':
                        user.email = None
                    else:
                        user.email = form.email.data
                    user.role_id = form.role_id.data
                    #TODO: add default password in settings
                    user.set_password("password")
                    user.is_superuser = 0
                    user.created_by = "{} {}".format(current_user.fname,current_user.lname)
                    db.session.add(user)
                    db.session.commit()
                    flash('New User Added Successfully!','success')
                    create_log("New user added","UserID={}".format(user.id))
                    return redirect(url_for(url))
                else:
                    for key, value in form.errors.items():
                        flash(str(key) + str(value), 'error')
                    return redirect(url_for(url))
        except Exception as e:
            flash(str(e),'error')
            return redirect(url_for(url))
    else:
        return render_template("auth/authorization_error.html")


@bp_auth.route('/user_edit/<int:oid>', methods=['GET', 'POST'])
@login_required
@cross_origin()
def user_edit(oid,**kwargs):
    user = User.query.get_or_404(oid)
    form = UserEditForm(obj=user)
    if request.method == "GET":
        user_permissions = UserPermission.query.filter_by(user_id=oid).all()
        query1 = db.session.query(UserPermission.model_id).filter_by(user_id=oid)
        models = db.session.query(CoreModel).filter(~CoreModel.id.in_(query1))
        form.model_inline.models = models
        form.permission_inline.models = user_permissions
        return admin_edit(form=form, update_url=auth_urls['edit'], action="auth/user_edit_action.html", \
            oid=oid, modal_form=True,extra_modal='auth/user_change_password_modal.html',model=User,kwargs=kwargs)
    elif request.method == "POST":
        if form.validate_on_submit():
            try:
                user.username = form.username.data
                user.fname = form.fname.data
                user.lname = form.lname.data
                user.email = form.email.data
                user.role_id = form.role_id.data
                user.updated_at = datetime.now()
                user.updated_by = "{} {}".format(current_user.fname,current_user.lname)
                db.session.commit()
                flash('User update Successfully!','success')
                create_log('User update',"UserID={}".format(oid))
                return redirect(url_for('bp_iwms.users'))
            except Exception as e:
                flash(str(e),'error')
                return redirect(url_for('bp_iwms.users'))
        for key, value in form.errors.items():
            flash(str(key) + str(value), 'error')
        return redirect(url_for('bp_iwms.users'))


@bp_auth.route('/user_edit_permission', methods=['POST'])
@cross_origin()
def user_edit_permission():
    if request.method == 'POST':
        permission_id = request.json['permission_id']
        read = request.json['read']
        create = request.json['create']
        write = request.json['write']
        delete = request.json['delete']
        permission = UserPermission.query.get(permission_id)
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


@bp_auth.route('/user_add_permission/<int:oid>/', methods=['POST'])
@login_required
def user_add_permission(oid):
    if request.method == "POST":
        user = User.query.get_or_404(oid)
        model = CoreModel.query.filter_by(id=request.args.get('model_id')).first()
        read, create, write, delete = request.form.get('chk_read', 0), request.form.get('chk_create', 0), \
            request.form.get('chk_write', 0), request.form.get('chk_delete', 0)

        if read == 'on':
            read = 1
        if create == 'on':
            create = 1
        if write == 'on':
            write = 1
        if delete == 'on':
            delete = 1

        permission = UserPermission(user_id=user.id, model=model, read=read, create=create, write=write, delete=delete)
        user.permissions.append(permission)
        db.session.commit()
        load_permissions(current_user.id)
        return redirect(url_for(auth_urls['edit'], oid=oid))


@bp_auth.route('/user_delete_permission/<int:oid>/', methods=['POST'])
@login_required
def user_delete_permission(oid):
    if request.method == "POST":
        try:
            permission = UserPermission.query.get(oid)
            db.session.delete(permission)
            db.session.commit()
            load_permissions(current_user.id)
            return redirect(request.referrer)
        except Exception as e:
            db.session.rollback()
