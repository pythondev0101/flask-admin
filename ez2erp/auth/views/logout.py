from flask import redirect, url_for
from flask_login import logout_user, login_required
from ez2erp.auth import bp_auth



@bp_auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('bp_auth.login'))
