 
from flask import (jsonify, abort, request, make_response)
from app import auth, db
from . import bp_bds
from .models import Delivery


@bp_bds.route('/api/v1.0/deliveries', methods=['GET'])
def get_deliveries():

    _get_deliveries = Delivery.query.all()

    # SERIALIZE MODELS
    _list = []
    for delivery in _get_deliveries:
        _list.append({
            'id': delivery.id,
            'date': delivery.date,
            'reference_number': delivery.reference_number
        })

    # WE SERIALIZE AND RETURN LIST INSTEAD OF MODELS 
    return jsonify({'deliveries': _list})


# @bp_api.route('/v1.0/users/<int:id>', methods=['GET'])
# @auth.login_required
# def get_user(id):
#     """ ENDPOINT: /api/v1.0/users/<user_id>
#     """

#     _user = User.query.get_or_404(id)
#     if _user is None:
#         abort(404)
    
#     return jsonify({
#         'id': _user.id,
#         'username': _user.username})


@bp_bds.route('/api/v1.0/deliveries', methods=['POST'])
def create_delivery():

    if not request.json:
        abort(400)
    
    _date = request.json['date']
    _longitude = request.json['longitude']
    _latitude = request.json['latitude']
    _accuracy = request.json['accuracy']
    
    _new = Delivery()
    _new.date = _date
    _new.longitude = _longitude
    _new.latitude = _latitude
    _new.accuracy = _accuracy

    
    db.session.add(_new)
    db.session.commit()

    return jsonify({'result':True
    })


# @bp_api.route('/v1.0/user/<int:id>', methods=['PUT'])
# @auth.login_required
# def update_user(id):

#     _user = User.query.get_or_404(id)
    
#     if _user is None:
#         abort(404)
    
#     if not request.json:
#         abort(404)

#     if not 'username' in request.json and type(request.json['username']) != str:
#         abort(404)

#     _username = request.json['username']
#     _role = request.json['role']
#     _user.username = _username
#     db.session.commit()

#     return jsonify({
#         'id': _user.id,
#         'username': _user.username
#     })


# @bp_api.route("/v1.0/user/<int:id>", methods=["DELETE"])
# @auth.login_required
# def delete_user(id):
#     _user = User.query.get_or_404(id)

#     if _user is None:
#         abort(404)

#     db.session.delete(value)
#     db.session.commit()

#     return jsonify({
#         "Result": True
#         })
