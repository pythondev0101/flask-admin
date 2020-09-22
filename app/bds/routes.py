from flask import render_template, flash, redirect, url_for, request, jsonify, \
    current_app, session,g
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import db, context

from . import bp_bds


@bp_bds.route('/')
@bp_bds.route('/dashboard')
@login_required
def dashboard():
    context['module'] = 'bds'
    return render_template('bds/bds_dashboard.html',context=context, title="Dashboard")