""" MODULE: AUTH.ROUTES """

""" FLASK IMPORTS """
from flask import render_template, flash, redirect, url_for, request,jsonify,current_app
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
import base64
"""--------------END--------------"""

""" APP IMPORTS  """
from app.auth import bp_auth
from app import login_manager
from app import db
"""--------------END--------------"""

""" MODULE: AUTH,ADMIN IMPORTS """
from .models import User
from .forms import LoginForm, UserCreateForm
"""--------------END--------------"""

""" URL IMPORTS """
from app.admin import admin_urls
from app.core import core_urls
from app.auth import auth_urls
from app import system_models
"""--------------END--------------"""

""" TEMPLATES IMPORTS """
from . import auth_templates
"""--------------END--------------"""


# TODO: AJAX for checking names
# @app.route('/user_check', methods=['POST'])
# def username_check():
#     conn = None
#     cursor = None
#     try:
#         username = request.form['username']
#
#         # validate the received values
#         if username and request.method == 'POST':
#             conn = mysql.connect()
#             cursor = conn.cursor(pymysql.cursors.DictCursor)
#             cursor.execute("SELECT * FROM user WHERE login_username=%s", username)
#             row = cursor.fetchone()
#
#             if row:
#                 resp = jsonify('<span style=\'color:red;\'>Username unavailable</span>')
#                 resp.status_code = 200
#                 return resp
#             else:
#                 resp = jsonify('<span style=\'color:green;\'>Username available</span>')
#                 resp.status_code = 200
#                 return resp
#         else:
#             resp = jsonify('<span style=\'color:red;\'>Username is required field.</span>')
#             resp.status_code = 200
#             return resp
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


@bp_auth.route('/user_create', methods=['POST'])
def user_create():
    user_create_form = UserCreateForm()
    if request.method == "POST":
        if user_create_form.validate_on_submit():
            user = User()
            user.username = user_create_form.username.data
            user.fname = user_create_form.fname.data
            user.lname = user_create_form.lname.data
            user.email = user_create_form.email.data
            user.set_password(user_create_form.password.data)
            print("MYDEBUG!!!")
            print("active:",user.active)
            print("created_at:",user.created_at)
            print("image_path:",user.image_path)
            print(dir(user))
            print("MYDEBUG!!!")
            db.session.add(user)
            db.session.commit()
            flash('New User Added Successfully!')
            return redirect(url_for(auth_urls['index']))
        else:
            return redirect(url_for(auth_urls['index']))


@bp_auth.route('/users')
def index():
    page = request.args.get('page', 1, type=int)
    data_per_page = current_app.config['DATA_PER_PAGE']
    users = User.query.paginate(page,data_per_page,False)
    user_create_form = UserCreateForm()
    next_url = url_for(auth_urls['index'], page=users.next_num) \
        if users.has_next else None
    prev_url = url_for(auth_urls['index'], page=users.prev_num) \
        if users.has_prev else None
    context = {
        'title': 'Users',
        'system_models': system_models,
        'users': users.items,
        'active': 'Users',
        'forms': {'UserCreateForm':user_create_form},
        'next_url': next_url,
        'prev_url': prev_url,
        'data_per_page': data_per_page,
    }
    return render_template(auth_templates['index'],context=context)


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Instance of auth.forms.loginform
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for(admin_urls['admin']))
        # TODO: make templates dictionary
        return render_template('auth/user_login.html', title='Log In', form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for(auth_urls['login']))
            else:
                login_user(user, remember=form.remember_me.data)
                # flash('Login request for user {}, remember_me={}'.format(form.username.data,form.remember_me.data))
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for(admin_urls['admin'])
                return redirect(url_for(admin_urls['admin']))


@bp_auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(core_urls['index']))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.request_loader
def load_user_from_request(request):

    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # next, try to login using Basic Auth
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key)
        except TypeError:
            pass
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None

