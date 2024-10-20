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

bp_ofic = Blueprint('oficios_routes', __name__)
cors = CORS()
cors.init_app(bp_ofic, resources={r"*": {"origins": "*"}})

mongo_url = environ.get('MONGO_URL', 'mongodb://localhost:27017')
database_name = environ.get('MONGO_DB', 'ggame')

connect(db=database_name, host=mongo_url, alias="default")

@bp_ofic.route('/addOficio', methods=['POST'])
@jwt_required()  # Verify that the user is logged in
def addoficios():
    folio = request.form.get('folio', None)
    oficio = request.form.get('oficio', None)
    estatus = request.form.get('estatus')
    fechaOficio = request.form.get('fechaOficio', None)
    #imagen_url = request.files.get('imagen_url', None)
    
    archivos = request.files.getlist('imagen_url')
    nombres_archivos = []
    contenidos_imagenes = []

    for archivo in archivos:
        if archivo.filename == '':
            continue

        nombre_archivo = secure_filename(archivo.filename)
        contenido_imagen = archivo.read()

        nombres_archivos.append(nombre_archivo)
        contenidos_imagenes.append(contenido_imagen)
    
    if oficio is None or fechaOficio is None or folio is None:
        return jsonify({"msg": "Falta un campo requerido"}), 400
    
    if Oficios.find_one(oficio=oficio) is not None:    # Checking if the username already exists
        return jsonify({"msg": "Oficio ya existe"}), 400
    
    ofic = Oficios(oficio=oficio, fechaOficio=fechaOficio, folio=folio, estatus="Carga Inicial", imagen_name=nombres_archivos, imagen=contenidos_imagenes)
    ofic.save()
    
    return jsonify({'result': 'ok'}), 201

#TODO
@bp_ofic.route('/updateOficio', methods=['PATCH']) 
@jwt_required()
def update_oficio():
    
    oficio = request.form.get('oficio', None)
    folio = request.form.get('folio', None)
    
    current_identity = get_jwt_identity()

    current_user = Oficio.find_one(id=ObjectId(current_identity))
    
    if oficio is not None and folio is not None:
        if Oficio.find_one(oficio=oficio):
            return jsonify({"msg": "Desired 'oficio' has already been taken"}), 400
        current_oficio.username = new_username

    current_oficio.save()

    return jsonify({"msg": "'Oficio' updated successfully!"}), 200

@bp_ofic.route('/oficios', methods=['GET'])
@jwt_required()  # Verify that the user is logged in
def oficios():
    oficcs = []
    identity = get_jwt_identity()
    ofic = Oficios.objects(estatus='Carga Inicial')
    if not ofic:
        return jsonify({"msg": "Oficios no encontrados"}), 404
    for off in ofic:
        # Si 'off.imagen' es un array de imágenes, lo convertimos a base64
        imagenes_base64 = [base64.b64encode(imagen).decode('utf-8') if imagen else None for imagen in off.imagen]
        # 'off.imagen_name' puede ser directamente serializable si es un array de strings
        oficcs.append({
            "oficio": off.oficio, 
            "folio": off.folio, 
            "fechaOficio": off.fechaOficio, 
            "estatus": off.estatus,
            "imagen": imagenes_base64,
            "imagen_name": off.imagen_name  # Aquí asumimos que es un array de strings, lo que es serializable
        })
    return jsonify({"data": oficcs}), 200

@bp_ofic.route('/oficiosM2', methods=['GET'])
@jwt_required()  # Verify that the user is logged in
def oficiosM2():
    oficcs = []
    identity = get_jwt_identity()
    ofic = Oficios.objects(estatus='Pendiente de Folio')
    if not ofic:
        return jsonify({"msg": "Oficios no encontrados"}), 404
    for off in ofic:
        oficcs.append({
            "oficio": off.oficio, "folio": off.folio, "fechaOficio": off.fechaOficio, "estatus": off.estatus
        })
    return jsonify({"data": oficcs}), 200

@bp_ofic.route('/oficiosM3', methods=['GET'])
@jwt_required()  # Verify that the user is logged in
def oficiosM3():
    oficcs = []
    identity = get_jwt_identity()
    ofic = Oficios.objects(estatus='En Evaluacion')
    if not ofic:
        return jsonify({"msg": "Oficios no encontrados"}), 404
    for off in ofic:
        oficcs.append({
            "oficio": off.oficio, "folio": off.folio, "fechaOficio": off.fechaOficio, "estatus": off.estatus
        })
    return jsonify({"data": oficcs}), 200

@bp_ofic.route('/oficiosM4', methods=['GET'])
@jwt_required()  # Verify that the user is logged in
def oficiosM4():
    oficcs = []
    identity = get_jwt_identity()
    ofic = Oficios.objects(estatus='En Evaluacion Externa')
    if not ofic:
        return jsonify({"msg": "Oficios no encontrados"}), 404
    for off in ofic:
        oficcs.append({
            "oficio": off.oficio, "folio": off.folio, "fechaOficio": off.fechaOficio, "estatus": off.estatus
        })
    return jsonify({"data": oficcs}), 200

@bp_ofic.route('/oficiosM5', methods=['GET'])
@jwt_required()  # Verify that the user is logged in
def oficiosM5():
    oficcs = []
    identity = get_jwt_identity()
    ofic = Oficios.objects(estatus='Observado')
    if not ofic:
        return jsonify({"msg": "Oficios no encontrados"}), 404
    for off in ofic:
        oficcs.append({
            "oficio": off.oficio, "folio": off.folio, "fechaOficio": off.fechaOficio, "estatus": off.estatus
        })
    return jsonify({"data": oficcs}), 200

@bp_ofic.route('/oficiosM6', methods=['GET'])
@jwt_required()  # Verify that the user is logged in
def oficiosM6():
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