""" MODULE: ADMIN.ROUTES """
""" FLASK IMPORTS """
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required

"""--------------END--------------"""

""" APP IMPORTS  """
from app import system_models
from app.admin import bp_admin
"""--------------END--------------"""

""" TEMPLATES IMPORTS """
from . import admin_templates
"""--------------END--------------"""


@bp_admin.route('/')
@login_required
def index():
    # TODO: return total tables,users...
    context = {
        'title': 'Admin',
        'system_models': system_models,
        'active': 'main_dashboard',
    }
    return render_template(admin_templates['index'], context=context)
