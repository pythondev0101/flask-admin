from ez2erp import CONTEXT
from ez2erp.core.models import App
from ez2erp.admin import bp_admin
from ez2erp.admin.templating import Page, PageConfig, Sidebar, SidebarItem, Breadcrumb



@bp_admin.route('/apps')
def apps():
    page_config = PageConfig(
        template="admin/admin_wingo_apps.html",
        sidebar=Sidebar([
            SidebarItem(
                'Apps',
                'bp_admin.apps'
            )
        ])
    )
    breadcrumb = Breadcrumb(
        title='Apps',
        parent='ez2erp',
        child='Apps'
    )
    page = Page(config=page_config, breadcrumb=breadcrumb)
    _apps = App.query.all()
    return page.display(apps=_apps)
