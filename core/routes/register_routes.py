# from tkinter import *
# from PIL import ImageTk, Image
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from core.models.user import User
from core.models.notification import Notification
from core.models.oficios import Oficios
from core.models.registro import Registro
from mongoengine import connect
from bson import ObjectId
from os import environ
from flask_cors import CORS
import base64

bp_reg = Blueprint('register_routes', __name__)
cors = CORS()
cors.init_app(bp_reg, resources={r"*": {"origins": "*"}})

mongo_url = environ.get('MONGO_URL', 'mongodb://localhost:27017')
database_name = environ.get('MONGO_DB', 'ggame')

connect(db=database_name, host=mongo_url, alias="default")


@bp_reg.route('/register', methods=['POST'])
def register():
    username = request.form.get('username', None)
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    completeName = request.form.get('completeName', None)
    
    if username is None or password is None or email is None:
        return jsonify({"msg": "Missing username, password, or email"}), 400
    
    if User.find_one(username=username) is not None:    # Checking if the username already exists
        return jsonify({"msg": "User already exists"}), 400
    
    if User.find_one(email=email) is not None:  # Checking if the email already exists
        return jsonify({"msg": "User already exists"}), 400
    
    user = User(username=username, password=password, email=email, completeName=completeName, active=False, rol=["su"])
    user.save()
    
    return jsonify({'result': 'ok'}), 201

@bp_reg.route('/registerEmail', methods=['POST'])
def registerEmail():
    email = request.form.get('email', None)
    
    if email is None:
        return jsonify({"msg": "Missing email"}), 400
    
    if User.find_one(email=email) is not None:  # Checking if the email already exists
        return jsonify({"msg": "Correo electrónico ya existe como usuario"}), 400
    
    if Registro.find_one(email=email) is not None:    # Checking if the username already exists
        return jsonify({"msg": "Correo electrónico ya existe"}), 400
    
    regis = Registro(email=email, active=False)
    regis.save()
    
    return jsonify({'result': 'ok'}), 201

@bp_reg.route('/getRegisterEmail', methods=['GET'])
def getRegisterEmail():
    regs = []
    registers = Registro.objects(active=False)
    if not registers:
        return jsonify({"msg": "Registros no encontrados"}), 404
    for reg in registers:
        regs.append({
            "email": reg.email, 
            "created_at": reg.created_at
        })
    
    return jsonify({"data": regs}), 200