from app.auth import auth_urls
from app.admin import admin_urls
from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user



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


from . import cli


"""Base class for modules"""


class CoreModule:

    no_admin_models = []
    
    background_app = False

    sidebar = None

    @property
    def module_name(self):
        raise NotImplementedError('Must implement module_name')

    @property
    def module_short_description(self):
        raise NotImplementedError('Must implement module_short_description')

    @property
    def module_long_description(self):
        raise NotImplementedError('Must implement module_long_description')

    @property
    def module_link(self):
        raise NotImplementedError('Must implement module_link')

    @property
    def module_icon(self):
        raise NotImplementedError('Must implement module_icon')

    @property
    def models(self):
        raise NotImplementedError('Must implement models')

    @property
    def version(self):
        raise NotImplementedError('Must implement version')
