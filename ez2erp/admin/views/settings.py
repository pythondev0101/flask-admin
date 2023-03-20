from flask import redirect, url_for, render_template
from flask_login import login_required
from ez2erp.admin import bp_admin
from ez2erp.admin.templating import Page, PageConfig, Sidebar, SidebarItem
from ez2erp.auth.models import User



sidebar = Sidebar(
    items=[
        SidebarItem(
            name='General Settings',
            link='bp_auth.users'
        ),
        SidebarItem(
            name='Users',
            link='bp_admin.users'
        )
    ]
)

@bp_admin.route('/settings')
def settings():
    page_config = PageConfig(
        template="admin/admin_wingo_settings.html",
        sidebar=sidebar
    )
    page = Page.blank(config=page_config)
    return page.display()


@bp_admin.route('/settings/users')
def users():
    page = Page.table(
        User,
        columns=[User.id, User.username, User.fname, User.lname, User.email]
    )
    return page.display()

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
