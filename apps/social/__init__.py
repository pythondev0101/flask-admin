from flask import Blueprint



bp_social = Blueprint(
    'bp_social', __name__, template_folder='templates',
    static_folder='static', static_url_path='/social/static'
)

from . import models
