from flask import Flask
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from os import environ
from datetime import timedelta

# load environment variables
load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY', 'super-secret')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15) # but days=30

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)

from core.routes.auth_routes import bp # import blueprint
app.register_blueprint(bp) # register blueprint