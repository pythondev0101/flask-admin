from ez2erp import CONTEXT
from ez2erp.core.models import CoreModule
from ez2erp.admin import bp_admin
from ez2erp.admin.templating import admin_render_template
from ez2erp.admin.models import AdminApp



@bp_admin.route('/apps')
def apps():
    modules = CoreModule.query.all()

    return admin_render_template(AdminApp, 'admin/admin_apps.html', 'admin', title='Apps',modules=modules)
