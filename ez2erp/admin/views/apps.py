from ez2erp import CONTEXT, APPS
from ez2erp.core.models import App
from ez2erp.admin import bp_admin
from ez2erp.admin.templating import Page, PageConfig, Breadcrumb



@bp_admin.route('/apps')
def apps():
    page_config = PageConfig(
        template="admin/admin_wingo_apps.html",
        sidebar=[
            App
        ]
    )
    breadcrumb = Breadcrumb(
        title='Apps',
        parent='ez2erp',
        child='Apps'
    )
    page = Page(config=page_config, breadcrumb=breadcrumb)
    _apps = APPS
    return page.display(apps=_apps)
