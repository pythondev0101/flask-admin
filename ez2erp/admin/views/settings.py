from flask import redirect, url_for, request, flash
from flask_login import login_required
from ez2erp.core.models import Model
from ez2erp.admin import bp_admin
from ez2erp.admin.templating import Page, PageConfig, SidebarItem, Breadcrumb, notify
from ez2erp.auth.models import User, Role
from ez2erp.admin.forms import Form, Input, Table
from ez2erp.db.query import Query
from bson import ObjectId



# sidebar = Sidebar(
#     items=[
#         SidebarItem(
#             name='Back to Home',
#             link='bp_admin.dashboard',
#             icon='corner-up-left'
#         ),
#         SidebarItem(
#             name='General Settings',
#             link='bp_admin.general_settings'
#         ),
#         SidebarItem(
#             name='Users',
#             link='bp_admin.users'
#         ),
#         SidebarItem(
#             name='Roles',
#             link='bp_admin.roles'
#         )
#     ]
# )

sidebar = [
    SidebarItem(
        name='Back to Home',
        link='bp_admin.dashboard',
        icon='corner-up-left'
    ),
    SidebarItem(
        name='General Settings',
        link='bp_admin.general_settings'
    ),
    User,
    Role
]


@bp_admin.route('/settings/general')
def general_settings():
    page_config = PageConfig(
        template="admin/admin_wingo_settings.html",
        sidebar=sidebar
    )
    breadcrumb = Breadcrumb(
        title='General Settings',
        parent='Admin',
        child='General Settings'
    )
    page = Page.blank(config=page_config, breadcrumb=breadcrumb)
    return page.display()


@bp_admin.route('/settings/users')
def users():
    page_config = PageConfig(sidebar=sidebar)
    columns = [User.id, User.username, User.fname, User.lname, User.email, User.status]
    return Page.table(
        User,
        columns=columns,
        create_function="bp_admin.create_user",
        config=page_config
    )


@bp_admin.route('/settings/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == "GET":
        form = Form.create(
            inputs=[
                [
                    Input.text(User.username, required=True),
                    Input.email(User.email, required=True),
                ],
                [
                    Input.text(User.fname, required=True),
                    Input.text(User.lname, required=False),
                    Input.text(User.contact_no, required=True)
                ],
                [
                    Input.select(
                        User.role,
                        required=True
                    )
                ]
            ]
        )
        page_config = PageConfig(sidebar=sidebar)
        page = Page.create(User, form=form, config=page_config)
        return page.display()
    elif request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        contact_no = request.form.get('contact_no')
        role = request.form.get('role')

        new_user = User({
            'username': username,
            'email': email,
            'fname': fname,
            'lname': lname,
            'contact_no': contact_no,
            'role': ObjectId(role)
        })
        new_user.save()
        flash('User created successfully!', 'success')
        return redirect(url_for('bp_admin.users'))
    

@bp_admin.route('/settings/roles')
def roles():
    page_config = PageConfig(sidebar=sidebar)
    return Page.table(
        Role,
        columns=[Role.id, Role.name, Role.created_at, Role.created_by],
        config=page_config,
        with_actions=True,
        create_function="bp_admin.create_role",
        edit_function='bp_admin.edit_role'
    )


@bp_admin.route('/settings/roles/create')
def create_role():
    if request.method == "GET":
        form = Form.create(
            inputs=[
                [
                    Input.text(Role.name, required=True),
                    Input.text(Role.description)
                ]
            ],
        )
        page_config = PageConfig(sidebar=sidebar)
        return Page.create(Role, form=form, config=page_config)
    elif request.method == "POST":
        pass


@bp_admin.route('/settings/roles/<string:oid>/edit',methods=['GET','POST'])
@login_required
def edit_role(oid):    
    if request.method == "GET":
        all_permissions = []
        existing_permissions = Role.query.find_one({'_id': ObjectId(oid)}).document.get('permissions', [])
        models = Model.query.all()
        for model in models:
            all_permissions.append({'id': str(model.id), 'name': model.name})

        for permission in all_permissions:
            for existing_permission in existing_permissions:
                if permission['name'] == existing_permission['name']:
                    permission['create'] = existing_permission['create']
                    permission['read'] = existing_permission['read']
                    permission['update'] = existing_permission['update']
                    permission['delete'] = existing_permission['delete']
            else:
                permission['create'] = False
                permission['read'] = False
                permission['update'] = False
                permission['delete'] = False

        form = Form.edit(
            inputs=[
                [
                    Input.text('name', label='Name', required=True),
                    Input.text('description', label='Description', required=True),
                ]
            ],
            cards_html=[
                "admin/custom/role_permission_inline.html"
            ]
        )
        page_config = PageConfig(sidebar=sidebar)
        return Page.edit(Role, oid, form=form, config=page_config)
        # return page.display(all_permissions=all_permissions)
    elif request.method == "POST":
        name = request.form.get('name')
        description = request.form.get('description')

        Query(Role).collection.update_one({'_id': ObjectId(oid)}, {
            '$set': {
                'name': name,
                'description': description
            }
        })
        notify('Role updated Successfully!', 'success')
        return redirect(url_for('bp_admin.roles'))


# form = UserForm()
# # fields = [User.id, User.username, User.fname, User.lname, Role.name, User.email]
# fields = ['id', 'username', 'fname', 'lname', 'role', 'email']
# models = [User]

# _users = User.objects

# _table_data = []

# for user in _users:
#     _table_data.append((
#         user.id,
#         user.username,
#         user.fname,
#         user.lname,
#         user.role.name,
#         user.email
#     ))

# return admin_table(*models, fields=fields, form=form, create_url='bp_auth.create_user',\
#     edit_url="bp_auth.edit_user", table_data=_table_data, view_modal_url='/auth/get-view-user-data', **options)
