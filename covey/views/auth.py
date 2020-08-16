# covey/views/auth.py

from flask import Blueprint, request, jsonify

from extensions import bcrypt
from covey.dal.users import add_user, get_user_by_email

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/register', methods=['POST'])
def create_user():
    params = request.get_json()
    username = params.get("username")
    email = params.get("email")
    password = params.get("password")

    user = get_user_by_email(email)
    if user:
        return jsonify({'message': 'Sorry, that email already exists'}), 400

    user = add_user(username, email, password)
    return jsonify(user), 201


@auth_blueprint.route('/login', methods=['POST'])
def login():
    params = request.get_json()
    email = params.get("email")
    password = params.get("password")

    user = get_user_by_email(email)
    if not user:
        return jsonify({'message': 'User does not exist'}), 404
    elif not bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Incorrect password'}), 400
    access_token = user.encode_token()
    return jsonify(access_token=access_token), 200
