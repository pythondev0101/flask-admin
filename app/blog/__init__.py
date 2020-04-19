from flask import Blueprint

bp_blog = Blueprint('bp_blog', __name__,)

blueprint_name = "bp_blog"  # The name of the module's blueprint
module_name = "blog"  # The name of the module

# URLS DICTIONARY
# NOTE: CHANGE (model) to your module's model eg. customer_create
blog_urls = {
    'index': '{}.index'.format(blueprint_name),
    'create': '{}.(model)_create'.format(blueprint_name),
    'edit': '{}.(model)_edit'.format(blueprint_name),
    'delete': '{}.(model)_delete'.format(blueprint_name),
}

# TEMPLATES DICTIONARY
# NOTE: CHANGE (model) to your module's model eg. customer_create.html
blog_templates = {
    'index': '{}/blog_index.html'.format(module_name),
    'create': '{}/post_create.html'.format(module_name),
    'edit': '{}/post_edit.html'.format(module_name),
}

from . import routes
from . import models

from .models import Post



class BlogModule:
    module_name = 'blog'
    module_icon = 'fa-rss-square'
    module_link = 'bp_blog.index'
    module_description = 'Blog'
    models = [Post]