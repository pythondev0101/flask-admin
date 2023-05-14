from flask import redirect, url_for, request, flash
from flask_login import login_required
from ez2erp.admin import bp_admin
from ez2erp.admin.templating import Page, PageConfig, Sidebar, SidebarItem, Breadcrumb
from ez2erp.auth.models import User, Role
from ez2erp.auth.models import Role
from ez2erp.admin.templating import Page, PageConfig
from ez2erp.admin.forms import Form, Input
from ez2erp.db.query import Query
from bson import ObjectId



sidebar = Sidebar(
    items=[
        SidebarItem(
            name='General Settings',
            link='bp_admin.general_settings'
        ),
        SidebarItem(
            name='Users',
            link='bp_admin.users'
        ),
        SidebarItem(
            name='Roles',
            link='bp_admin.roles'
        )
    ]
)

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
    page = Page.table(
        User,
        columns=[User.id, User.username, User.fname, User.lname, User.email],
        config=page_config,
    )
    return page.display()


@bp_admin.route('/settings/roles')
def roles():
    page_config = PageConfig(sidebar=sidebar)
    page = Page.table(
        Role,
        columns=[Role.id, Role.name, Role.created_at, Role.created_by],
        config=page_config,
        with_actions=True,
        edit_url='bp_admin.edit_role'
    )
    return page.display()


@bp_admin.route('/settings/roles/<string:oid>/edit',methods=['GET','POST'])
@login_required
def edit_role(oid):    
    if request.method == "GET":
        form = Form.edit(
            inputs=[
                [
                    Input.text('name', label='Name', required=True),
                    Input.text('description', label='Description', required=True),
                ]
            ]
        )
        page_config = PageConfig(sidebar=sidebar)
        page = Page.edit(Role, oid, form=form, config=page_config)
        return page.display()

    elif request.method == "POST":
        name = request.form.get('name')
        description = request.form.get('description')

        Query(Role).collection.update_one({'_id': ObjectId(oid)}, {
            '$set': {
                'name': name,
                'description': description
            }
        })

        flash('Role updated Successfully!','success')
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
