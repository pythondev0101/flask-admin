from . import models
from app.auth import auth_urls
from app.admin import admin_urls
from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user
import click
# URLS DICTIONARY
core_urls = {
    'index': 'core.index',
}


bp_core = Blueprint('core', __name__)


@bp_core.route('/')
def index():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for(admin_urls['admin']))
        else:
            return redirect(url_for(auth_urls['login']))

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


@bp_core.cli.command("create_module")
@click.argument("module_name")
def create_module(module_name):
    # TODO: FOR FUTURE VERSION CHECK OS
    # For windows only
    try:
        import os
        from config import basedir
        from shutil import copyfile
        import platform

        if platform.system() == "Windows":
            module_path = basedir + "\\app" + "\\" + module_name
            templates_path = basedir + "\\app" + "\\" + module_name + "\\" + "templates" + "\\" + module_name 
            core_init_path = basedir + "\\app" + "\\core" + \
                "\\module_template" + "\\__init__.py"
            core_models_path = basedir + "\\app" + \
                "\\core" + "\\module_template" + "\\models.py"
            core_routes_path = basedir + "\\app" + \
                "\\core" + "\\module_template" + "\\routes.py"
        elif platform.system() == "Linux":
            module_path = basedir + "/app" + "/" + module_name
            templates_path = basedir + "/app" + "/" + module_name + "/templates" + "/" + module_name
            core_init_path = basedir + "/app" + "/core" + "/module_template" + "/__init__.py"
            core_models_path = basedir + "/app" + "/core" + "/module_template" + "/models.py"
            core_routes_path = basedir + "/app" + "/core" + "/module_template" + "/routes.py"

        core_file_list = [core_init_path, core_models_path, core_routes_path]

        if not os.path.exists(module_path):
            os.mkdir(module_path)
            os.makedirs(templates_path)
            for file_path in core_file_list:
                file_name = os.path.basename(file_path)
                copyfile(file_path, os.path.join(module_path, file_name))
    except OSError as e:
        print("Creation of the directory %s failed" % module_path)
        print(e)
    else:
        print("Successfully created the directory %s " % module_path)