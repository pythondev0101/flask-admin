""" MODULE: ADMIN.ROUTES """
""" FLASK IMPORTS """
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required

"""--------------END--------------"""

""" APP IMPORTS  """
from app import system_modules
from app.admin import bp_admin
"""--------------END--------------"""

""" TEMPLATES IMPORTS """
from . import admin_templates
"""--------------END--------------"""
from . import context


def change_context(view):
    # VALUES: title, module, active, forms, modal
    context['module'] = 'admin'
    if view == 'index':
        context['title'] = 'Admin'
        context['active'] = 'main_dashboard'
        context['modal'] = False


@bp_admin.route('/')
@login_required
def index():
    # TODO: return total tables,users...
    change_context('index')
    return render_template(admin_templates['index'], context=context)
