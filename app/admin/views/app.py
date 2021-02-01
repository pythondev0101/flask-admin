from app import CONTEXT
from app.core.models import CoreModule
from app.admin import bp_admin, admin_render_template



@bp_admin.route('/apps')
def apps():
    modules = CoreModule.query.all()

    CONTEXT['active'] = 'apps'

    return admin_render_template('admin/admin_apps.html', 'admin', title='Apps',modules=modules)
