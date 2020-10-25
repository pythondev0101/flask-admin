from flask import render_template, flash, redirect, url_for, request, jsonify, \
    current_app, session,g
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import db, context
from . import bp_bds
from .models import Delivery, Area, Subscriber, Messenger
from .forms import *
from app.admin.routes import admin_index
from app.auth.models import User


@bp_bds.route('/')
@bp_bds.route('/dashboard')
@login_required
def dashboard():
    context['module'] = 'bds'
    context['active'] = 'main_dashboard'
    return render_template('bds/bds_dashboard.html',context=context, title="Dashboard",)


@bp_bds.route('/areas')
@login_required
def areas():
    fields = [Area.id,Area.name, Area.code, Area.description]
    form = AreaForm()
    context['create_modal']['create_url'] = False

    return admin_index(Area, fields=fields,form=form,create_modal=True,template='bds/bds_table.html',\
        edit_url="bp_bds.area_edit")


@bp_bds.route('/area_create',methods=['GET','POST'])
@login_required
def area_create():
    form = AreaCreateForm()

    if request.method == "GET":

        subscribers = Subscriber.query.all()        
        messengers = User.query.filter_by(role_id=2).all()
        context['module'] = 'bds'
        context['model'] = 'area'

        return render_template('bds/bds_area_create.html',context=context,form=form,title="Create area", subscribers=subscribers,messengers=messengers)
    elif request.method == "POST":
        if form.validate_on_submit():
            area = Area()
            area.name = form.name.data
            area.code = form.code.data
            area.description = form.description.data

            subscribers_line = request.form.getlist('subscribers[]')
            if subscribers_line:
                for sub_id in subscribers_line:
                    subscriber = Subscriber.query.get_or_404(int(sub_id))
                    area.subscribers.append(subscriber)

            messengers_line = request.form.getlist('messengers[]')
            if messengers_line:
                for mes_id in messengers_line:
                    messenger = User.query.get_or_404(int(mes_id))
                    area.messengers.append(messenger)

            db.session.add(area)
            db.session.commit()
            flash('New Area added Successfully!','success')
            return redirect(url_for('bp_bds.areas'))
        else:
            for key, value in f.errors.items():
                flash(str(key) + str(value), 'error')
            return redirect(url_for('bp_bds.areas'))


@bp_bds.route('/area_edit/<int:oid>', methods=['GET','POST'])
@login_required
def area_edit(oid):
    area = Area.query.get_or_404(oid)
    form = AreaCreateForm(obj=area)
    if request.method == "GET":
        context['module'] = 'bds'
        context['model'] = 'area'

        subscribers = Subscriber.query.all()

        return render_template('bds/bds_area_edit.html',context=context,form=form,title="Edit area",oid=oid,\
            subscribers=subscribers,area=area)
    elif request.method == "POST":
        if form.validate_on_submit():
            area.name = form.name.data
            area.code = form.code.data
            area.description = form.description.data

            subscribers_line = request.form.getlist('subscribers[]')
            area.subscribers = []

            if subscribers_line:
                for sub_id in subscribers_line:
                    subscriber = Subscriber.query.get_or_404(int(sub_id))
                    area.subscribers.append(subscriber)

            messengers_line = request.form.getlist('messengers[]')
            area.messengers = []
            if messengers_line:
                for mes_id in messengers_line:
                    messenger = User.query.get_or_404(int(mes_id))
                    area.messengers.append(messenger)

            db.session.add(area)
            db.session.commit()
            flash('Area updated Successfully!','success')
            return redirect(url_for('bp_bds.areas'))
        else:
            for key, value in f.errors.items():
                flash(str(key) + str(value), 'error')
            return redirect(url_for('bp_bds.areas'))



@bp_bds.route('/subscribers')
@login_required
def subscribers():
    fields = [Subscriber.id, Subscriber.fname,Subscriber.lname]
    form = SubscriberForm()
    return admin_index(Subscriber, fields=fields, form=form, template='bds/bds_table.html',create_url="bp_bds.subscriber_create")


@bp_bds.route('/subscriber_create',methods=['POST'])
@login_required
def subscriber_create():
    form = SubscriberForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            s = Subscriber()
            s.fname = form.fname.data
            s.lname = form.lname.data
            s.email = form.email.data
            s.addresss = form.address.data
            s.area_id = form.area_id.data
            s.longitude = form.longitude.data
            s.latitude = form.latitude.data

            db.session.add(s)
            db.session.commit()
            flash('New subscriber added successfully!','success')
            return redirect(url_for('bp_bds.subscribers'))
        else:
            for key, value in form.errors.items():
                flash(str(key) + str(value), 'error')
            return redirect(url_for('bp_bds.subscribers'))


@bp_bds.route('/messengers',methods=['GET'])
@login_required
def messengers():
    form = MessengerForm()
    fields = [User.id, User.username, User.fname, User.lname, User.email]
    models = [User]
    query = User.query.with_entities(*fields).filter_by(role_id=2).all()
    return admin_index(*models, fields=fields, url="bp_bds.messengers", create_url='bp_bds.messenger_create', edit_url="bp_auth.user_edit", form=form,\
    kwargs={'module': 'bds','models':query}, template="bds/bds_table.html")


@bp_bds.route('/messenger_create', methods=['POST'])
@login_required
def messenger_create():
    form = MessengerForm()
    if form.validate_on_submit():
        m = User()
        m.fname = form.fname.data
        m.lname = form.lname.data
        m.email = form.email.data
        m.username = form.username.data
        m.area_id = form.area_id.data
        m.role_id = 2
        m.set_password("password")
        m.is_superuser = 0
        db.session.add(m)
        db.session.commit()
        flash('New messenger added successfully!','success')
        return redirect(url_for('bp_bds.messengers'))
    else:
        for key, value in form.errors.items():
            flash(str(key) + str(value), 'error')
        return redirect(url_for('bp_bds.messengers'))


@bp_bds.route('/deliveries',methods=['GET'])
@login_required
def deliveries():
    areas = Area.query.all()
    subscribers = Subscriber.query.all()
    
    context['active'] = 'delivery'
    context['model'] = 'delivery'
    context['module'] = 'bds'

    return render_template('bds/bds_delivery.html',context=context,title="Delivery", areas=areas, subscribers=subscribers)


@bp_bds.route('/create_delivery', methods=['POST'])
@login_required
def create_delivery():
    subscribers_line = request.form.getlist('subscribers[]')
    if subscribers_line:
        for sub_id in subscribers_line:
            new = Delivery()
            new.subscriber_id = int(sub_id)
            new.status = "IN-PROGRESS"
            new.active = True

            db.session.add(new)
            db.session.commit()

    flash('Deliver successfully', 'success')
    return redirect(url_for('bp_bds.deliveries'))


@bp_bds.route('/reset_delivery/<int:area_id>', methods=['GET'])
@login_required
def reset_delivery(area_id):

    area = Area.query.get_or_404(area_id)
    print(area)

    for subscriber in area.subscribers:
        delivery = Delivery.query.filter_by(subscriber_id=subscriber.id, active=1).first()

        print(delivery)
        delivery.active = 0
        db.session.commit()

    flash("Delivery reset successfully", 'success')
    return redirect(url_for('bp_bds.deliveries'))