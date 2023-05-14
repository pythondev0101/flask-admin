from werkzeug.urls import url_parse
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_user, logout_user, login_required
from ez2erp import CONTEXT
from ez2erp.auth import bp_auth
from ez2erp.auth.forms import LoginForm
from ez2erp.admin import admin_urls
from ez2erp.auth import auth_urls
from ez2erp.auth import auth_templates
from ez2erp.auth.models import User
from ez2erp.auth.permissions import load_permissions



@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for(admin_urls['admin']))
        return render_template("auth/auth_wingo_login.html", \
            title=current_app.config['ADMIN']['APPLICATION_NAME'])
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        # user = User.objects(username=username).first()
        user = User.query.retrieve("640e9e70bc80fda287276af2")
        if user is None or not user.check_password(password):
            flash('Invalid username or password','error')
            return redirect(url_for(auth_urls['login']))

        login_user(user, remember=False)
        print(user)
        load_permissions(user.id)
        
        next_page = request.args.get('next')
        
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for(current_app.config['AUTH']['LOGIN_REDIRECT_URL'])
        return redirect(next_page)
