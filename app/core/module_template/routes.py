# """ ROUTES """
#
# """ FLASK IMPORTS """
# from flask import render_template, flash, redirect, url_for, request, jsonify, current_app
# from flask_login import current_user, login_user, logout_user, login_required
# from werkzeug.urls import url_parse
# import base64
#
# """--------------END--------------"""
#
# """ APP IMPORTS  """
# from app.module import bp_module
# from app import db
#
# """--------------END--------------"""
#
# """ MODULE: AUTH,ADMIN IMPORTS """
# from .models import YourModel
#
# """--------------END--------------"""
#
# """ URL IMPORTS """
# from . import module_urls
#
# """--------------END--------------"""
#
# """ TEMPLATES IMPORTS """
# from . import module_templates
#
# """--------------END--------------"""
#

#
#
# @bp_module.route('/')
# @login_required
# def index():
#     return render_template(module_templates['index'], context=context)
#
#
# @bp_module.route('/model_edit/<int:id>')
# @login_required
# def model_create(id):
#     # Place your code here
#     pass
#
#
# @bp_module.route('/model_delete/<int:id>',methods=['DELETE'])
# @login_required
# def model_create(id):
#     # Place your code here
#     pass
