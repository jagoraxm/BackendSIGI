from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
from core.models.user import User
from mongoengine import connect
from bson import ObjectId
from os import environ

bp = Blueprint('user_routes', __name__)

mongo_url = environ.get('MONGO_URL', 'mongodb://localhost:27017')
database_name = environ.get('MONGO_DB', 'ggame')

connect(db=database_name, host=mongo_url, alias="default")


@bp.route('/register', methods=['POST'])
def register():
    username = request.form.get('username', None)
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    
    if username is None or password is None or email is None:
        return jsonify({"msg": "Missing username, password, or email"}), 400
    
    if User.find_one(username=username) is not None:    # Checking if the username already exists
        return jsonify({"msg": "Username already exists"}), 400
    
    if User.find_one(email=email) is not None:  # Checking if the email already exists
        return jsonify({"msg": "Email already exists"}), 400
    
    user = User(username=username, password=password, email=email)
    user.save()
    
    return jsonify({'result': 'ok'}), 201



@bp.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', None)
    password = request.form.get('password', None)

    user = User.find_one(username=username)

    if user is None or not check_password_hash(user.password, password):  # Password verification
        return jsonify({"msg": "Bad username or password"}), 401

    # Convert the ObjectId to a string
    user_id_str = str(user.id)

    return jsonify(access_token=create_access_token(identity=user_id_str)), 200



@bp.route('/checkAuth', methods=['GET'])
@jwt_required()  # Verify that the user is logged in
def check_auth():
    identity = get_jwt_identity()
    user = User.find_one(id=ObjectId(identity))
    if not user:
        return jsonify({"msg": "User not found"}), 404
    return jsonify({"username": user.username, "email": user.email}), 200



@bp.route('/logout', methods=['POST'])
@jwt_required()  # Verify that the user is logged in
def logout():
    return jsonify({"msg": "Successfully logged out"}), 200



@bp.route('/updateProfile', methods=['PATCH'])
@jwt_required()
def update_profile():
    new_username = request.form.get('new_username', None)

    current_identity = get_jwt_identity()

    current_user = User.find_one(id=ObjectId(current_identity))

    if new_username is not None:
        if User.find_one(username=new_username):
            return jsonify({"msg": "Desired username has already been taken"}), 400

        current_user.username = new_username

    current_user.save()

    return jsonify({"msg": "Profile updated successfully!"}), 200