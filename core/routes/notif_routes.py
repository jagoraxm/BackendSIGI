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

bp_notif = Blueprint('notif_routes', __name__)
cors = CORS()
cors.init_app(bp_notif, resources={r"*": {"origins": "*"}})

mongo_url = environ.get('MONGO_URL', 'mongodb://localhost:27017')
database_name = environ.get('MONGO_DB', 'ggame')

connect(db=database_name, host=mongo_url, alias="default")

@bp_notif.route('/notifications', methods=['GET'])
@jwt_required()  # Verify that the user is logged in
def notifications():
    """Endpoint para obtener notificaciones
    ---
    tags:
      - Notif
    """
    identity = get_jwt_identity()
    user = Notification.find_one(id=ObjectId(identity))
    if not user:
        return jsonify({"msg": "User not found"}), 404
    return jsonify({"username": user.username, "email": user.email}), 200

@bp_notif.route('/notifications', methods=['POST'])
@jwt_required()  # Verify that the user is logged in
def notification():
    """Endpoint para insertar notificaciones
    ---
    tags:
      - Notif
    """
    title = request.form.get('title', None)
    description = request.form.get('description', None)
    #action = request.form.get('action', None)
    priority = request.form.get('priority', None)
    active = request.form.get('active', None)
    
    if title is None or description is None or priority is None:
        return jsonify({"msg": "Missing field in request"}), 400
    
    if Notification.find_one(title=title) is not None:    # Checking if the username already exists
        return jsonify({"msg": "Notification exists"}), 400
    
    notif = Notification(title=title, description=description, priority=priority, active=True)
    notif.save()
    
    return jsonify({'result': 'ok'}), 201

    oficcs = []
    identity = get_jwt_identity()
    ofic = Oficios.objects(estatus='Elaboracion Respuesta P/N')
    if not ofic:
        return jsonify({"msg": "Oficios no encontrados"}), 404
    for off in ofic:
        oficcs.append({
            "oficio": off.oficio, "folio": off.folio, "fechaOficio": off.fechaOficio, "estatus": off.estatus
        })
    return jsonify({"data": oficcs}), 200