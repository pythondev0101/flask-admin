from flask import redirect, url_for
from flask_login import login_required
from ez2erp.admin import bp_admin
from ez2erp.admin.models import AdminDashboard
from ez2erp.admin.templating import Page, PageConfig, SidebarItem, Breadcrumb



@bp_admin.route('/dashboard')
@login_required
def dashboard():
    if AdminDashboard.__view_url__ == 'bp_admin.no_view_url':
        return redirect(url_for('bp_admin.no_view_url'))
    
    page_config = PageConfig(
        "admin/admin_wingo_dashboard.html")
    breadcrumb = Breadcrumb(
        title='Dashboard',
        parent='Admin',
        child='Dashboard'
    )
    page = Page.blank(page_config, breadcrumb=breadcrumb, is_main=True)
    return page.display()
