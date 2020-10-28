from flask import jsonify, abort, request
from app.auth import bp_auth
from .models import User, UserPermission, Role, RolePermission
from app import csrf
from flask_cors import cross_origin


@bp_auth.route('/api/users/login',methods=['POST'])
@csrf.exempt
@cross_origin()
def api_login():
    username = request.json['username']
    password = request.json['password']

    print(username,password)
    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        abort(401)

    return jsonify({'userData':{
        'id': user.id,
        'fname': user.fname,
        'lname': user.lname,
        'email': user.email}})


@bp_auth.route('/api/users', methods=['GET'])
def get_users():
    user_list = []
    users = User.query.all

    for user in users:
        user_list.append({
            'id': user.id,
            'fname': user.fname,
            'lname': user.lname,
            'email': user.email,
        })

    return jsonify({'users':user_list})

@bp_auth.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    
    if user is None:
        abort(404)

    return jsonify({
        'id': user.id,
        'fname': user.fname,
        'lname': user.lname,
        'email': user.email,
    })