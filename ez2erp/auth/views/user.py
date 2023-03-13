from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_required
from flask_cors import cross_origin
from ez2erp import db
from ez2erp.core.models import CoreModel
from ez2erp.core.logging import create_log
from ez2erp.auth import bp_auth
from ez2erp.auth.models import User, UserPermission, Role
from ez2erp.auth.forms import UserForm, UserEditForm, UserPermissionForm
from ez2erp.auth import auth_urls
from ez2erp.auth.permissions import load_permissions, check_create
from ez2erp.admin.templating import admin_table, admin_edit



@bp_auth.route('/users')
@login_required
def users(**options):
    form = UserForm()
    # fields = [User.id, User.username, User.fname, User.lname, Role.name, User.email]
    fields = ['id', 'username', 'fname', 'lname', 'role', 'email']
    models = [User]

    _users = User.objects

    _table_data = []

    for user in _users:
        _table_data.append((
            user.id,
            user.username,
            user.fname,
            user.lname,
            user.role.name,
            user.email
        ))
    
    return admin_table(*models, fields=fields, form=form, create_url='bp_auth.create_user',\
        edit_url="bp_auth.edit_user", table_data=_table_data, view_modal_url='/auth/get-view-user-data', **options)


@bp_auth.route('/get-view-user-data', methods=['GET'])
@login_required
def get_view_user_data():
    _column, _id = request.args.get('column'), request.args.get('id')

    _data = User.objects(id=_id).values_list(_column)

    response = jsonify(result=str(_data[0]),column=_column)

    if _column == "role":
        response = jsonify(result=str(_data[0].id),column=_column)

    response.headers.add('Access-Control-Allow-Origin', '*')
    response.status_code = 200
    return response


@bp_auth.route('/users/create', methods=['POST'])
@login_required
def create_user(**kwargs):

    if not check_create('Users'):
        return render_template("auth/authorization_error.html")

    form = UserForm()

    url = auth_urls['users']

    if 'url' in kwargs:
        url = kwargs.get('url')

    if not form.validate_on_submit():
        for key, value in form.errors.items():
            flash(str(key) + str(value), 'error')
        return redirect(url_for(url))   

    try:
        user = User()
        # models = CoreModel.objects

        # for model in models:
        #     permission = UserPermission(
        #         model=model, 
        #         read=True,
        #         create=False,
        #         write=False,
        #         doc_delete=False
        #         )
        #     user.permissions.append(permission)

        user.username = form.username.data
        user.fname = form.fname.data
        user.lname = form.lname.data

        if form.email.data == '':
            user.email = None
        else:
            user.email = form.email.data
        
        print(form.role.data)
        user.role = Role.objects.get(id=form.role.data)

        #TODO: add default password in settings
        user.set_password("password")
        user.is_superuser = False
        user.created_by = "{} {}".format(current_user.fname,current_user.lname)
        
        user.save()

        flash('New User Added Successfully!','success')
        create_log("New user added","UserID={}".format(user.id))

        return redirect(url_for(url))

    except Exception as e:
        flash(str(e),'error')
        return redirect(url_for(url))


@bp_auth.route('/users/<string:oid>/edit', methods=['GET', 'POST'])
@login_required
@cross_origin()
def edit_user(oid,**kwargs):
    user = User.objects.get_or_404(id=oid)
    form = UserEditForm(obj=user)

    if request.method == "GET":
        # user_permissions = UserPermission.query.filter_by(user_id=oid).all()
        # form.permission_inline.data = user_permissions

        _scripts = [
            {'bp_auth.static': 'js/auth.js'},
            {'bp_admin.static': 'js/admin_edit.js'}
        ]

        return admin_edit(User, form, auth_urls['edit'], oid, auth_urls['users'],action_template="auth/user_edit_action.html", \
            modals=['auth/user_change_password_modal.html'], scripts=_scripts, **kwargs)
    
    if not form.validate_on_submit():
        for key, value in form.errors.items():
            flash(str(key) + str(value), 'error')
        return redirect(url_for(auth_urls['users']))
        
    try:

        user.username = form.username.data
        user.fname = form.fname.data
        user.lname = form.lname.data
        user.email = form.email.data if not form.email.data == '' else None
        user.role = Role.objects.get(id=form.role.data)
        user.updated_at = datetime.now()
        user.updated_by = "{} {}".format(current_user.fname,current_user.lname)
        
        user.save()
        flash('User update Successfully!','success')
        create_log('User update',"UserID={}".format(oid))

    except Exception as e:
        flash(str(e),'error')
    
    return redirect(url_for(auth_urls['users']))


@bp_auth.route('/permissions')
@login_required
def user_permission_index():
    fields = [UserPermission.id, User.username, User.fname, CoreModel.name, UserPermission.read, UserPermission.create,
              UserPermission.write, UserPermission.delete]
    model = [UserPermission, User,CoreModel]
    form = UserPermissionForm()
    return admin_table(*model, fields=fields, form=form, list_view_url=auth_urls['user_permission_index'], create_modal=False,
                       view_modal=False, active="Users")


@bp_auth.route('/username_check', methods=['POST'])
def username_check():
    if request.method == 'POST':
        username = request.json['username']
        user = User.objects(username=username).first()
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
        user = User.objects(email=email).first()
        if user:
            resp = jsonify(result=0)
            resp.status_code = 200
            return resp
        else:
            resp = jsonify(result=1)
            resp.status_code = 200
            return resp


@bp_auth.route('/change_password/<string:oid>',methods=['POST'])
def change_password(oid):
    user = User.query.get_or_404(oid)
    user.set_password(request.form.get('password'))
    db.session.commit()
    flash("Password change successfully!",'success')
    return redirect(request.referrer)


@bp_auth.route('/users/<int:oid1>/permissions/<int:oid2>/edit', methods=['POST'])
@cross_origin()
def edit_permission(oid1, oid2):

    permission_type = request.json['permission_type']
    value = request.json['value']

    permission = UserPermission.query.get_or_404(oid2)

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
