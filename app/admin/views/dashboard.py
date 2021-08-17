from flask import redirect, url_for
from flask_login import login_required
from app.core.models import CoreModule, CoreModel
from app.admin import bp_admin
from app.admin.models import AdminDashboard
from app.admin.templating import admin_dashboard, DashboardBox


@bp_admin.route('/') # move to views
@login_required
def dashboard():
    from app.auth.models import User

    if AdminDashboard.__view_url__ == 'bp_admin.no_view_url':
        return redirect(url_for('bp_admin.no_view_url'))
    
    options = {
        'box1': DashboardBox("Total Modules","Installed",CoreModule.objects.count()),
        'box2': DashboardBox("System Models","Total models",CoreModel.objects.count()),
        'box3': DashboardBox("Users","Total users",User.objects.count())
    }

    return admin_dashboard(AdminDashboard, **options)
