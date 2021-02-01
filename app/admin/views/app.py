from app import CONTEXT
from app.core.models import CoreModule
from app.admin import bp_admin
from app.admin.templating import admin_render_template
from app.admin.models import AdminApp



@bp_admin.route('/apps')
def apps():
    modules = CoreModule.query.all()

    return admin_render_template(AdminApp, 'admin/admin_apps.html', 'admin', title='Apps',modules=modules)
