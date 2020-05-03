from flask import Blueprint

bp_blog = Blueprint('bp_module', __name__,)


from . import routes
from . import models
