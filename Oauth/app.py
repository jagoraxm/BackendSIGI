# python modules
from flask_openapi3 import Info, HTTPBearer, OpenAPI
from werkzeug.utils import redirect

from flask_cors import CORS

# constants
from constants.routes import SWAGGER_URL
from config import Settings

# services
from services.logger_service import logger
from services.authorization_service import Authorization

# apps
from apps.login import appLogin
from apps.registry import appRegistry

config = Settings()


def create_app():
    # OpenAPI config
    info = Info(title="Service App Espacio Extract Banner, API", version="0.0.10")
    jwt = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    security_schemes = {"jwt": jwt}

    # set app using OpenAPI
    app = OpenAPI(__name__, info=info, security_schemes=security_schemes)

    CORS(app)
    cors = CORS(app, resource={
        r"/service/api/*":{
            "origins":"http://localhost:5173/"
        }
    })

    # setup with the configuration provided
    app.config["ENVIRONMENT"] = config.environment
    app.config["DEBUG"] = config.debug
    app.config["TESTING"] = config.testing
    app.config["SECRET_KEY"] = config.secret_key

    # AUTHORIZATION MIDDLEWARE
    app.wsgi_app = Authorization(app.wsgi_app)

    # register apps
    app.register_api(appLogin)
    app.register_api(appRegistry)

    @app.route("/")
    def redirect_to_swagger():
        return redirect(SWAGGER_URL)

    return app


if __name__ == "__main__":
    logger.info(f"{config.service_name} running at port: {config.port}")
    create_app().run(host=config.host, port=config.port)
