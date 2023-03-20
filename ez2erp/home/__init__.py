from flask import Blueprint



bp_home = Blueprint('bp_home',__name__,template_folder='templates',\
    static_folder='static', static_url_path='/home/static')


from . import views