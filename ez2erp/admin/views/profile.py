from ez2erp.admin import bp_admin
from ez2erp.admin.templating import Page, PageConfig, SidebarItem, Breadcrumb
from ez2erp.auth.models import User



@bp_admin.route('/profile/<string:user_id>')
def profile(user_id):
    user = User.query.retrieve(user_id)

    breadcrumb = Breadcrumb(title='Profile', parent='Admin', child='Profile')
    page_config = PageConfig(template='admin/admin_wingo_profile.html')
    page = Page(config=page_config, breadcrumb=breadcrumb)
    return page.display(user=user)
