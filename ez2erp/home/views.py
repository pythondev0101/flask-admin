from flask import request, redirect, url_for
from flask_login import current_user
from ez2erp.auth import auth_urls
from ez2erp.admin import admin_urls
from ez2erp.home import bp_home



@bp_home.route('/')
def index():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for(admin_urls['admin']))
        else:
            return redirect(url_for(auth_urls['login']))
