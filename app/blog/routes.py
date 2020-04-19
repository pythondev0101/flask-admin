""" ROUTES """

""" FLASK IMPORTS """
from flask import render_template, flash, redirect, url_for, request, jsonify, current_app
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import base64

"""--------------END--------------"""

""" APP IMPORTS  """
from app.blog import bp_blog
from app import db, context

"""--------------END--------------"""

""" MODULE: AUTH,ADMIN IMPORTS """
from .models import Post

"""--------------END--------------"""

""" URL IMPORTS """
from . import blog_urls

"""--------------END--------------"""

""" TEMPLATES IMPORTS """
from . import blog_templates

"""--------------END--------------"""
from datetime import datetime
from app.admin.routes import admin_index

# This function will change context values depends in view
def change_context(view):
    # VALUES: title, module, active, forms, modal
    context['module'] = 'blog'
    if view == 'index':
        context['title'] = 'Blog'
        context['active'] = 'Posts'
        context['modal'] = True


@bp_blog.route('/')
def index():
    if current_user.is_authenticated:
        posts = Post.query.filter_by(user_id=current_user.id).all()
        print(posts)
        change_context('index')
        return render_template(blog_templates['index'], context=context,posts=posts)
    else:
        posts = Post.query.all()
        change_context('index')
        return render_template(blog_templates['index'], context=context,posts=posts)


@bp_blog.route('/post_create',methods=['GET','POST'])
@login_required
def post_create():
    if request.method == "GET":
        return render_template(blog_templates['create'], context=context)
    elif request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        post = Post()
        post.user_id = int(current_user.id)
        post.post_title = title
        post.content = content
        db.session.add(post)
        db.session.commit()
        flash("Post added successfully!")
        return redirect(url_for(blog_urls['index']))


@bp_blog.route('/post_edit')
@login_required
def post_edit():
    if request.method == "GET":
        fields = [Post.id,Post.post_title,Post.created_at,Post.updated_at]
        return admin_index(Post,fields=fields,url=blog_urls['index'],create_modal=False,
                           view_modal=False,template='blog/post_edit_index.html')


@bp_blog.route('/post_update/<int:post_id>',methods=['GET','POST'])
@login_required
def post_update(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == "GET":
        return render_template(blog_templates['edit'],post=post,context=context)
    elif request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        post.post_title = title
        post.content = content
        post.updated_at = datetime.utcnow()
        db.session.commit()
        flash("Post update successfully!")
        return redirect(url_for(blog_urls['index']))


@bp_blog.route('/post_destroy/<int:post_id>',methods=['POST'])
@login_required
def post_destroy(post_id):
    try:
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted successfully!')
        return redirect(url_for(blog_urls['index']))
    except Exception as e:
        context['errors'] = {'Delete error','A problem occured'}
        db.session.rollback()
        return redirect(url_for(blog_urls['index']))


@bp_blog.route('/post_delete',methods=['GET','POST'])
@login_required
def post_delete():
    if request.method == "GET":
        fields = [Post.id, Post.post_title, Post.created_at, Post.updated_at]
        return admin_index(Post, fields=fields, url=blog_urls['index'], create_modal=False,
                           view_modal=False, template='blog/post_delete_index.html')