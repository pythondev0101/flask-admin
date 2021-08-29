from functools import wraps
from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request, current_app
from flask_cors import cross_origin

import jwt

from app.auth.models import User
from app.auth import bp_auth
from app import csrf



@bp_auth.route('/register', methods=["POST"])
def vue_register():
    data =request.get_json()

    user = User()
    user.username = data['username']
    user.set_password(data['password'])
    user.save()

    return jsonify(user.to_dict), 201

@bp_auth.route('/login', methods=['POST'])
@cross_origin()
@csrf.exempt
def vue_login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401

    token = jwt.encode({
        'sub': user.email,
        'iat': datetime.utcnow(),
        'exp':datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'],
        algorithm='HS256'
    )
    
    return jsonify({'token': token})
