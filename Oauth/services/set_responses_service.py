import copy
import json

from flask import jsonify, Response
from services.secure_service import decrypt_check_pass
from werkzeug.exceptions import abort
from services.logger_service import logger
from config import Settings

config = Settings()


service_response = {
    "service": {"id": config.service_id, "name": config.service_name},
    # "partialResponse": {},
    "data": {},
    "status": {},
}


def error_response_auth(status_code: int, error_info: str, status_info: str = None):
    """
    Sets Error Response
    """
    error_response_obj = copy.deepcopy(service_response)
    if status_info is not None:
        error_response_obj["status"] = {"info": status_info}
    error_response_obj["error"] = {"id": status_code, "info": error_info}

    return error_response_obj


def error_response(status_code: int, error_info: str, status_info: str = None):
    """
    Sets Error Response
    """
    error_response_obj = copy.deepcopy(service_response)
    if status_info is not None:
        error_response_obj["status"] = {"info": status_info}
    error_response_obj["error"] = {"id": status_code, "info": error_info}

    return abort(
        Response(
            json.dumps(error_response_obj),
            mimetype="application/json",
            status=status_code,
        )
    )


def post_successful_response(email: str, ticket_number: str, transaction_number: str, procedure: str):
    """
    Sets Successful Response
    """
    logger.debug(f"{email} - Salesforce response was successful")
    status_info = f"'{procedure}' was successfully requested to Salesforce service"
    logger.info(f"{email} - SSCES answered correctly with a ticket number and a transaction number")
    ok_response = copy.deepcopy(service_response)
    ok_response["data"] = {
        "ticketNumber": ticket_number,
        "transactionNumber": transaction_number,
    }
    ok_response["status"] = {"id": 201, "info": status_info}
    return ok_response


def error_object(status_id: int, message: str):
    """
    Sets an object error when something wrong happens
    """
    error_obj = {"error": True, "message": message, "status_code": status_id}
    return error_obj


def successful_response_method(data, status_info, status_code):
    ok_response = copy.deepcopy(service_response)
    ok_response["data"] = data
    if status_info is not None:
        ok_response["status"] = {"info": status_info}
    return ok_response, status_code

def succesful_response_login(usuarioPass, password):
    """
    Sets Successful Response
    """
    if (usuarioPass == 'Error'):
        return error_response_auth(403, "Usuario o contraseña incorrecta", "Usuario o contraseña incorrecta")
    else:
        logger.debug(f"{usuarioPass} - Login response was successful")
        status_info = f"Login response was successful"
        ok_response = copy.deepcopy(service_response)

        if decrypt_check_pass(usuarioPass, password):
            ok_response["data"] = {
                "user": "OK"
            }
            ok_response["status"] = {"id": 201, "info": status_info}
            return ok_response
        else:
            return error_response_auth(403, "Usuario o contraseña incorrecta", "Usuario o contraseña incorrecta")
    
def succesful_response_registry(rows):
    """
    Sets Successful Response Registry
    """
    logger.debug(f"{rows} - Registry response was successful")
    status_info = f"Registry response was successful"
    ok_response = copy.deepcopy(service_response)
    if rows > 0:
        ok_response["data"] = {
            "user": "OK"
        }
        ok_response["status"] = {"id": 201, "info": status_info}
        return ok_response
    else:
        return error_response_auth(403, "No se logro resgistrar el usuario", "No se logro resgistrar el usuario")