""" MODULE: AUTH.ROUTES """

""" FLASK IMPORTS """
from flask import render_template, flash, redirect, url_for, request, jsonify, \
    current_app, session,g
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import base64

"""--------------END--------------"""

""" APP IMPORTS  """
from app.auth import bp_auth
from app import db, context
"""--------------END--------------"""

""" MODULE: AUTH,ADMIN IMPORTS """
from .models import User, UserPermission
from .forms import LoginForm, UserForm, UserEditForm, UserPermissionForm
from app.core.models import HomeBestModel

"""--------------END--------------"""

""" URL IMPORTS """
from app.admin import admin_urls
from app.auth import auth_urls

"""--------------END--------------"""

""" TEMPLATES IMPORTS """
from . import auth_templates

"""--------------END--------------"""

from datetime import datetime
from flask_cors import cross_origin
from app.admin.routes import admin_index, admin_edit

context['module'] = 'admin'


# @bp_auth.route('/roles', methods=['GET', 'POST'])
# @login_required
# def role_index():
#     fields = [Role.id, Role.name, Role.created_at]
#     form = RoleCreateForm()
#     return admin_index(Role, fields=fields, url=auth_urls['role_index'],
#                        create_url='bp_auth.role_create', edit_url="bp_auth.user_edit", form=form)


@bp_auth.route('/permissions', methods=['GET', 'POST'])
@login_required
def user_permission_index():
    fields = [UserPermission.id, User.username, User.fname, HomeBestModel.name, UserPermission.read, UserPermission.create,
              UserPermission.write, UserPermission.delete]
    model = [UserPermission, User]
    form = UserPermissionForm()
    return admin_index(*model, fields=fields, form=form, url=auth_urls['user_permission_index'], create_modal=False,
                       view_modal=False, active="Users")


@bp_auth.route('/users')
@login_required
def index():
    form = UserForm()
    fields = [User.id, User.username, User.fname, User.lname, User.email]
    models = [User]
    return admin_index(*models, fields=fields, url=auth_urls['index'],
                       create_url='bp_auth.user_create', edit_url="bp_auth.user_edit", form=form)


# @bp_auth.route('/role_create', methods=['POST'])
# @login_required
# def role_create():
#     try:
#         role_create_form = RoleCreateForm()
#         if request.method == "POST":
#             if role_create_form.validate_on_submit():
#                 role = Role()
#                 role.name = role_create_form.name.data
#                 role.updated_at = datetime.now()
#                 db.session.add(role)
#                 db.session.commit()
#                 flash('New Role Added Successfully!')
#                 return redirect(url_for(auth_urls['role_index']))
#             else:
#                 for key, value in role_create_form.errors.items():
#                     print(key, value)
#                 return redirect(url_for(auth_urls['role_index']))
#     except Exception as e:
#         context['errors']['SystemError'] = e
#         return redirect(url_for(auth_urls['role_index']))


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


@bp_auth.route('/user_delete/<oid>', methods=['DELETE'])
def user_delete(user_id):
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()


@bp_auth.route('/user_create', methods=['POST'])
@login_required
def user_create():
    try:
        form = UserForm()
        if request.method == "POST":
            if form.validate_on_submit():
                user = User()
                models = HomeBestModel.query.all()
                for homebestmodel in models:
                    permission = UserPermission(model=homebestmodel, read=1,create=0, write=0, delete=0)
                    user.permissions.append(permission)
                user.username = form.username.data
                user.fname = form.fname.data
                user.lname = form.lname.data
                user.email = form.email.data
                user.set_password(form.password.data)
                user.is_superuser = 0
                db.session.add(user)
                db.session.commit()
                flash('New User Added Successfully!','success')
                return redirect(url_for(auth_urls['index']))
            else:
                for key, value in form.errors.items():
                    flash(key + value, 'error')
                return redirect(url_for(auth_urls['index']))
    except Exception as e:
        flash(str(e),'error')
        return redirect(url_for(auth_urls['index']))


@bp_auth.route('/user_edit/<int:oid>', methods=['GET', 'POST'])
@login_required
@cross_origin()
def user_edit(oid):
    user = User.query.get_or_404(oid)
    form = UserEditForm(obj=user)
    if request.method == "GET":
        user_permissions = UserPermission.query.filter_by(user_id=oid)
        query1 = db.session.query(UserPermission.model_id).filter_by(user_id=oid)
        models = db.session.query(HomeBestModel).filter(~HomeBestModel.id.in_(query1))
        form.model_inline.models = models
        form.permission_inline.models = user_permissions
        return admin_edit(form=form, update_url=auth_urls['edit'], action="auth/user_edit_action.html", \
            oid=oid, modal_form=True,extra_modal='auth/user_change_password_modal.html',model=User)
    elif request.method == "POST":
        if form.validate_on_submit():
            user.username = form.username.data
            user.fname = form.fname.data
            user.lname = form.lname.data
            user.email = form.email.data
            user.updated_at = datetime.now()
            db.session.commit()
            flash('User update Successfully!','success')
            return redirect(url_for(auth_urls['index']))
        for key, value in form.errors.items():
            print(key, value)
        return "error"


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
        model = HomeBestModel.query.filter_by(id=request.args.get('model_id')).first()
        read, create, write, delete = request.form.get('chk_read', 0), request.form.get('chk_create', 0), \
            request.form.get('chk_write', 0), request.form.get('chk_delete', 0)
        if read == 'on': read = 1
        if create == 'on': create = 1
        if write == 'on': write = 1
        if delete == 'on': delete = 1
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


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Instance of auth.forms.loginform

    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for(admin_urls['admin']))
        return render_template(auth_templates['login'], title=context['app_name'], form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password','success')
                return redirect(url_for(auth_urls['login']))
            else:
                login_user(user, remember=form.remember_me.data)
                load_permissions(user.id)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for(admin_urls['admin'])
                return redirect(url_for(admin_urls['admin']))


def load_permissions(user_id):
    user = User.query.get(user_id)
    if not user and not current_user.is_authenticated:
        context['system_modules'].pop('admin',None)
    
    user_permissions = UserPermission.query.filter_by(user_id=user_id)
    session.pop('permissions', None)
    if "permissions" not in session:
        session['permissions'] = {}
    if user:
        if user.is_superuser:
            all_permissions = HomeBestModel.query.all()
            for permission in all_permissions:
                session['permissions'][permission.name] = {"read": True, "create": True, \
                    "write": True, "delete": True}        
        else:
            for user_permission in user_permissions:
                session['permissions'][user_permission.model.name] = {"read": user_permission.read, "create": user_permission.create, \
                    "write": user_permission.write, "delete": user_permission.delete}
    print(session['permissions'])

@bp_auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))
