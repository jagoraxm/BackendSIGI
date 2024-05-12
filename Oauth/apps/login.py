# python modules
from flask_openapi3 import APIBlueprint, Tag
from flask import request as req

# OpenAPI
from OpenAPI.commons import (
    BadRequest,
    Unauthorized,
    Forbidden,
    NotFound,
    UnavailableService,
    Headers,
)
from OpenAPI.app_test_openapi import ResponseGet, ResponsePost, RequestBody

from services.set_responses_service import succesful_response_login

# constants
from constants.routes import APP_LOGIN_ROUTE

# services
from services.logger_service import logger

# repositories
from repositories.table_repository import find_all

from database.mysql.myDatabase import obtener_conexion

from services.secure_service import decrypt_check_pass

# library's


appLogin = APIBlueprint(
    "appLogin",
    __name__,
    url_prefix=APP_LOGIN_ROUTE,
    abp_tags=[Tag(name="appLogin", description="'appLogin' procedure")],
    abp_responses={
        "400": BadRequest,
        "401": Unauthorized,
        "403": Forbidden,
        "404": NotFound,
        "503": UnavailableService,
    },
)

@appLogin.get("", responses={"200": ResponseGet}, security=[{"jwt": []}])
def app_test_request_get(header: Headers):
    """
    Endpoint get example
    """
    name: str = "Lalo"

    logger.debug(f"Hola mundo desde flask{name}")

    print(f"Hola mundo desde flask{name}")

    # jecutando query
    # find_all(417531, 'ULA')

    return f"Hola mundo desde flask", 200

@appLogin.post("", responses={"201": ResponsePost}, security=[{"jwt": []}])
def app_login_request_post(header: Headers, body: RequestBody):
    """
    Endpoint post example
    """

    # auth_header = req.headers["Authorization"]

    print(f"Hola {body.email} desde flask")

    logger.debug(f"Hola {body.email} desde flask")

    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM user WHERE email = %s", (body.email))
        usuario = cursor.fetchone()
        print(f"User -> {usuario}")
        if (usuario != None):
            print(f"User -> {usuario[2]}")
            logger.debug(f"User -> {usuario[2]}")
            respuesta = succesful_response_login(usuario[1], body.password)
        else:
            respuesta = succesful_response_login('Error', body.password)
    conexion.close()

    return respuesta

