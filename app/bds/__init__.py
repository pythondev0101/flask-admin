from flask import Blueprint


bp_bds = Blueprint('bp_bds', __name__, template_folder='templates')


from . import routes, api
