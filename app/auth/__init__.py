from functools import wraps
from flask import Blueprint
from flask.globals import current_app, request
from flask.json import jsonify
import jwt



bp_auth = Blueprint('bp_auth',__name__,template_folder='templates',\
    static_folder='static', static_url_path='/auth/static')

blueprint_name = "bp_auth"  # The name of the module's blueprint
module_name = "auth"  # The name of the module

# URLS DICTIONARY
auth_urls = {
    'login': 'bp_auth.login',
    'users': 'bp_auth.users',
    'create': 'bp_auth.create_user',
    'edit': 'bp_auth.edit_user',
    'delete': 'bp_auth.user_delete',
    'user_permission_index': 'bp_auth.user_permission_index',
    'role_index': 'bp_auth.role_index',
}

# TEMPLATES DICTIONARY
auth_templates = {
    'login': 'auth/user_login.html',
    'edit': 'auth/user_edit.html',
    'user_permission_index': 'auth/user_permission_index.html',
    'role_index': 'auth/role_index.html',
}

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = models.User.objects(username=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify


from . import views
from . import models
from . import api


