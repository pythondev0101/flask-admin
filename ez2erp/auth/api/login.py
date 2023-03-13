from flask import jsonify, abort, request
from flask_cors import cross_origin
from ez2erp.auth import bp_auth
from ez2erp.auth.models import User
from ez2erp import csrf



@bp_auth.route('/api/users/login',methods=['POST'])
@csrf.exempt
def api_login():
    username = request.json['username']
    password = request.json['password']

    print(username,password)

    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        abort(401)

    response = jsonify({'userData':{
        'id': user.id,
        'fname': user.fname,
        'lname': user.lname,
        'email': user.email,
        'is_admin': user.is_admin}})
        
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


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
