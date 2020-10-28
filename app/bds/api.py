 
from flask import (jsonify, abort, request, make_response)
from app import auth, db
from . import bp_bds
from .models import Delivery, Subscriber, Area
from app import csrf
from flask_cors import cross_origin
from math import pi, cos, sqrt


@bp_bds.route('/api/confirm-deliver', methods=['POST'])
@csrf.exempt
@cross_origin()
def confirm_deliver():
    # FETCH DATA
    longitude = request.json['longitude']
    latitude = request.json['latitude']
    messenger_id = request.json['messenger_id']
    subscriber_id = request.json['subscriber_id']
    print(longitude, latitude)

    delivery = Delivery.query.filter_by(subscriber_id=subscriber_id,status="IN-PROGRESS").first()
    print(delivery)
    if delivery is None:
        abort(404)

    if _isCoordsNear(longitude, latitude, delivery.subscriber, 5):
        delivery.status = "DELIVERED"
    else:
        delivery.status = "PENDING"

    db.session.commit()
    return jsonify({'result':True})


def _isCoordsNear(checkPointLng, checkPointLat, centerPoint, km):
    ky = 40000 / 360
    kx = cos(pi * float(centerPoint.latitude) / 180.0) * ky
    dx = abs(float(centerPoint.longitude) - float(checkPointLng)) * kx
    dy = abs(float(centerPoint.latitude) - float(checkPointLat)) * ky
    print(sqrt(dx * dx + dy * dy) <= km)
    return sqrt(dx * dx + dy * dy) <= km 


@bp_bds.route('/api/send-image',methods=['POST'])
def process_image():
    img = request.files['image']

    coords = request.json['coords']

    subscriber_id = request.json['subscriber_id']
    messenger_id = request.json['messenger_id']


@bp_bds.route('/api/deliveries', methods=['GET'])
@csrf.exempt
@cross_origin()
def get_deliveries():
    _query = request.args.get('query')
    
    if _query == 'all':
        _get_deliveries = Delivery.query.filter_by(active=1).all()
    else:
        pass
        # _get_deliveries = Delivery.query.filter_by

    # SERIALIZE MODELS
    _list = []
    for delivery in _get_deliveries:
        _list.append({
            'id': delivery.id,
            'subscriber_id': delivery.subscriber.id,
            'subscriber_fname': delivery.subscriber.fname,
            'subscriber_lname': delivery.subscriber.lname,
            'delivery_date': delivery.delivery_date,
            'status': delivery.status,
            'longitude': delivery.subscriber.longitude,
            'latitude': delivery.subscriber.latitude            
        })

    # WE SERIALIZE AND RETURN LIST INSTEAD OF MODELS 
    return jsonify({'deliveries': _list})


@bp_bds.route('/api/subscribers', methods=['GET'])
@csrf.exempt
@cross_origin()
def get_subscribers():
    subscribers = Subscriber.query.all()

    _list = []
    
    for subscriber in subscribers:
        _delivery = Delivery.query.filter_by(subscriber_id=subscriber.id).first()
        _status = ""
        if _delivery:
            _status = _delivery.status

        _list.append({
            'id': subscriber.id,
            'fname': subscriber.fname,
            'lname': subscriber.lname,
            'address': subscriber.address,
            'status': _status
        })
    
    return jsonify({'subscribers': _list})


@bp_bds.route('/api/subscribers/<int:subscriber_id>', methods=['GET'])
@csrf.exempt
@cross_origin()
def get_subscriber(subscriber_id):
    subscriber = Subscriber.query.get_or_404(subscriber_id)

    if subscriber is None:
        abort(404)
    
    res = {
        'id': subscriber.id,
        'fname': subscriber.fname,
        'lname': subscriber.lname,
        'address': subscriber.address
    }

    return jsonify(res)


@bp_bds.route('/api/get-area-subscribers', methods=['GET'])
def get_area_subscribers():

    _area_name = request.args.get('area_name')
    area = Area.query.filter_by(name=_area_name).first()
    _res = []

    for subscriber in area.subscribers:

        delivery = Delivery.query.filter_by(subscriber_id=subscriber.id,active=1).first()

        _status = ""

        if delivery:
            _status = delivery.status
        else:
            _status = "NOT YET DELIVERED"

        _res.append({
            'id': subscriber.id,
            'fname': subscriber.fname,
            'lname': subscriber.lname,
            'address': subscriber.address,
            'status': _status
        })
    
    return jsonify({'subscribers': _res})


@bp_bds.route('/api/deliver', methods=['POST'])
def deliver():

    _area_name = request.json['area_name']
    area = Area.query.filter_by(name=_area_name).first()

    if area:
        for subscriber in area.subscribers:

            delivery = Delivery.query.filter_by(subscriber_id=subscriber.id,active=1).first()
            if delivery:
                pass
            #     if deliver.status == "DELIVERED":
            #         pass
            #     elif deliver.status == "IN-PROGRESS":
            #         pass
            #     elif deliver.status == "PENDING":
            #         pass

            else:
                new = Delivery()
                new.subscriber_id = subscriber.id
                new.status = "IN-PROGRESS"
                new.active = 1
                db.session.add(new)
                db.session.commit()

    return jsonify({'result': True})


@bp_bds.route('/api/reset', methods=['POST'])
def reset():
    _area_name = request.json['area_name']
    area = Area.query.filter_by(name=_area_name).first()

    if area is None:
        abort(404)
    
    for subscriber in area.subscribers:
        delivery = Delivery.query.filter_by(subscriber_id=subscriber.id,active=1).first()

        if delivery:
            delivery.active = 0
            db.session.commit()
    
    return jsonify({'result':True})



# @bp_bds.route('/api/v1.0/deliveries', methods=['POST'])
# def create_delivery():

#     if not request.json:
#         abort(400)
    
#     _date = request.json['date']
#     _longitude = request.json['longitude']
#     _latitude = request.json['latitude']
#     _accuracy = request.json['accuracy']
    
#     _new = Delivery()
#     _new.date = _date
#     _new.longitude = _longitude
#     _new.latitude = _latitude
#     _new.accuracy = _accuracy

    
#     db.session.add(_new)
#     db.session.commit()

#     return jsonify({'result':True
#     })
