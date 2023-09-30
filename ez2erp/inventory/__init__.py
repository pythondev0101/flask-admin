from flask import Blueprint



bp_inventory = Blueprint(
    'bp_inventory', __name__, template_folder='templates',
    static_folder='static', static_url_path='/inventory/static'
)


from . import models
