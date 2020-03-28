from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user

# URLS DICTIONARY
core_urls = {
    'index': 'bp_core.index',
}

from app.admin import admin_urls
from app.auth import auth_urls

bp_core = Blueprint('bp_core', __name__)




@bp_core.route('/')
def index():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for(admin_urls['admin']))
        else:
            return redirect(url_for(auth_urls['login']))
