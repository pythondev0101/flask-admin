""" MODELS """
""" FLASK IMPORTS """
from flask_login import UserMixin

"""--------------END--------------"""

""" PYTHON IMPORTS """
from werkzeug.security import generate_password_hash, check_password_hash

"""--------------END--------------"""

""" APP IMPORTS  """
from app import db
from app.core.models import Base

"""--------------END--------------"""

from datetime import datetime
from app.admin.models import Admin


# Sample model
class Post(Base, Admin):
    __tablename__ = 'blog_post'

    user_id = db.Column(db.Integer, db.ForeignKey('auth_user.id'))
    post_title = db.Column(db.String(64))
    content = db.Column(db.Text())
    index_fields = ['Title', 'Created at', 'updated at']
    index_title = "Posts"
    index_message = "Message"
    title = index_title
    model_name = 'Posts'
    model_icon = 'pe-7s-note'
    model_description = "POSTS"
    functions = {'Create post': 'bp_blog.post_create', 'View posts': 'bp_blog.index',
                 'Edit post': 'bp_blog.post_edit', 'Delete post': 'bp_blog.post_delete'}
