from flask import Flask
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from os import environ
from datetime import timedelta
from flask_mail import Mail
from flasgger import Swagger  # Importar Flasgger
import json

# load environment variables
load_dotenv()

mail = Mail()  # Inicializar extensión Flask-Mail

# Personaliza el codificador JSON
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        # Personaliza la serialización si es necesario
        return super().default(obj)

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY', 'super-secret')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1) # but days=30

    # Usar el codificador personalizado
    app.json_encoder = CustomJSONEncoder
    
    # Setup the Flask-JWT-Extended extension
    jwt = JWTManager(app)

    # Cargar la configuración
    app.config.from_object('config.Config')

    # Inicializar Flask-Mail
    mail.init_app(app)

    # Inicializar Flasgger (Swagger UI)
    Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Documentación de la API",
        "description": "API creada con Flask, JWT y Swagger",
        "version": "1.0.0",
        "contact": {
            "name": "Jonathan Arias García",
            "email": "jagoraxr.moucha@gmail.com"
        },
    },
    "host": "localhost:5000",  # Cambia esto a tu dominio en producción
    "basePath": "/",
})

    from core.routes.auth_routes import bp_auth # import blueprint
    from core.routes.register_routes import bp_reg # import blueprint
    from core.routes.oficios_routes import bp_ofic # import blueprint
    from core.routes.notif_routes import bp_notif # import blueprint
    app.register_blueprint(bp_auth) # register blueprint
    app.register_blueprint(bp_reg) # register blueprint
    app.register_blueprint(bp_ofic) # register blueprint
    app.register_blueprint(bp_notif) # register blueprint

    return app