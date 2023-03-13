from flask import render_template
from flask_login import login_required
from ez2erp.admin import bp_admin



@bp_admin.route('/notifications/no-url-view')
@login_required
def no_view_url():
    return render_template('admin/notifications/no_view_url.html'), 400