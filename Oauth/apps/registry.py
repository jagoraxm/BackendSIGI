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
from OpenAPI.app_test_openapi import ResponseGet, ResponsePost, RequestBody, RequestBodyReg

from services.set_responses_service import succesful_response_registry

# constants
from constants.routes import APP_REGISTRY_ROUTE

# services
from services.logger_service import logger

# repositories
from repositories.table_repository import find_all

from database.mysql.myDatabase import obtener_conexion

from services.secure_service import encrypt_password
# library's


appRegistry = APIBlueprint(
    "appRegistry",
    __name__,
    url_prefix=APP_REGISTRY_ROUTE,
    abp_tags=[Tag(name="appRegistry", description="'appRegistry' procedure")],
    abp_responses={
        "400": BadRequest,
        "401": Unauthorized,
        "403": Forbidden,
        "404": NotFound,
        "503": UnavailableService,
    },
)

@appRegistry.post("", responses={"201": ResponsePost}, security=[{"jwt": []}])
def app_registry_request_post(header: Headers, body: RequestBodyReg):
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
        if (usuario == None):
            cursor.execute(
                "INSERT INTO SIGI.user(password, email, nombre, apellido, idRol, idEstatus) VALUES(%s, %s, %s, %s, 0, 2)", (encrypt_password(body.password), body.email, body.nombre, body.apellido))
            print(f"Filas insertadas -> {cursor.rowcount}")

            logger.debug(f"Filas insertadas -> {cursor.rowcount}")
        
            respuesta = succesful_response_registry(cursor.rowcount)
            conexion.commit()
        else:
            respuesta = succesful_response_registry(0)
    conexion.close()

    return respuesta

