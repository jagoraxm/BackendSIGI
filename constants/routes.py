from config import Settings
from services.logger_service import logger


config = Settings()

SWAGGER_URL = "/openapi/swagger"
PREFIX = "/service/api/"

APP_LOGIN_ROUTE = PREFIX + "auth/v1"
APP_REGISTRY_ROUTE = PREFIX + "reg/v1" 

if config.host == "localhost":
    base_url = "http://" + config.host + ":" + str(config.port)
else:
    base_url = config.host
    logger.debug(f"base_url: {base_url}")

SERVICE_URLS = [
    APP_LOGIN_ROUTE, 
    APP_REGISTRY_ROUTE
]
