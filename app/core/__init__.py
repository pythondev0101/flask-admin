from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user
import click
# URLS DICTIONARY
core_urls = {
    'index': 'core.index',
}

from app.admin import admin_urls
from app.auth import auth_urls

bp_core = Blueprint('core', __name__)


@bp_core.route('/')
def index():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for(admin_urls['admin']))
        else:
            return redirect(url_for(auth_urls['login']))


from . import models

# Create Superuser command
@bp_core.cli.command('create_superuser')
def create_superuser():
    from app.auth.models import User
    from app import db
    user = User()
    user.fname = input("Enter First name: ")
    user.lname = input("Enter Last name: ")
    user.username = input("Enter Username: ")
    user.set_password(input("Enter password: "))
    user.is_superuser = 1
    user.email = ""
    db.session.add(user)
    db.session.commit()
    print("SuperUser Created!")