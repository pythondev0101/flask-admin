from flask import Blueprint

bp_blog = Blueprint('bp_module', __name__,)

blueprint_name = ""  # The name of the module's blueprint
module_name = ""  # The name of the module

# URLS DICTIONARY
# NOTE: CHANGE (model) to your module's model eg. customer_create
module_urls = {
    'index': '{}.index'.format(blueprint_name),
    'create': '{}.(model)_create'.format(blueprint_name),
    'edit': '{}.(model)_edit'.format(blueprint_name),
    'delete': '{}.(model)_delete'.format(blueprint_name),
}

# TEMPLATES DICTIONARY
# NOTE: CHANGE (model) to your module's model eg. customer_create.html
module_templates = {
    'index': '{}/(model)_index.html'.format(module_name),
    'create': '{}/(model)_create.html'.format(module_name),
    'edit': '{}/(model)_.html'.format(module_name),
}


from . import routes
from . import models
