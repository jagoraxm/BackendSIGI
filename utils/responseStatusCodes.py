"""
200 200 Ok Standard response to HTTP requests
201 201 Created Implies the request was fulfilled and a new
        resource has been created
204 204 No Content Successful request and no data has been returned
400 400 Bad Request Implies that the server can’t process the request
        due to a client error
403 403 Not Authorized Valid request but the requesting client is not
        authorized to obtain the resource
404 404 Not Found The requested resource doesn’t exist on the server
422 422 Unprocessable Entity Request can’t be processed due to semantic error
500 500 Internal Server Error Generic error to imply an unexpected condition in
        server

"""

INVALID_FIELD_NAME_SENT_422 = {
    "http_code": 422,
    "code": "invalidField",
    "message": "Invalid fields found",
}
INVALID_INPUT_422 = {
    "http_code": 422,
    "code": "invalidInput",
    "message": "Invalid input",
}
MISSING_PARAMETERS_422 = {
    "http_code": 422,
    "code": "missingParameter",
    "message": "Missing parameters.",
}
BAD_REQUEST_400 = {"http_code": 400, "code": "badRequest", "message": "Bad request"}
SERVER_ERROR_500 = {"http_code": 500, "code": "serverError", "message": "Server error"}
SERVER_ERROR_404 = {
    "http_code": 404,
    "code": "notFound",
    "message": "Resource not found",
}
UNAUTHORIZED_403 = {
    "http_code": 403,
    "code": "notAuthorized",
    "message": "You are not authorised to execute this.",
}

SUCCESS_200 = {"http_code": 200, "code": "success"}
SUCCESS_201 = {"http_code": 201, "code": "success"}
SUCCESS_204 = {"http_code": 204, "code": "success"}
