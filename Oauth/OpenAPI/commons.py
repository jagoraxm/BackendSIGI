from base64 import b64decode

from pydantic import BaseModel, Field, validator
from constants.messages import unavailable_option, unavailable_service_info
from typing import Optional
from config import Settings


config = Settings()


class Headers(BaseModel):
    service_id: str = Field(None, alias="Service-Id")
    service_name: str = Field(None, alias="Service-Name")


class BadRequest(BaseModel):
    error = {
        "id": 400,
        "name": "Bad Request",
        "message": "You have to provide a 'Service-Id, a 'Service-Name and an authorization access token.",
    }


class Unauthorized(BaseModel):
    service = {"id": config.service_id, "name": config.service_name}
    status = {}
    error = {"id": 401, "info": "Invalid access token"}


class Forbidden(BaseModel):
    service = {"id": config.service_id, "name": config.service_name}
    status = {}
    error = {"id": 403, "info": "Expired access token"}


class NotFound(BaseModel):
    service = {"id": config.service_id, "name": config.service_name}
    status = {"info": unavailable_option}
    error = {"id": 404, "info": "No se encontró la matrícula '12345' en salesforce"}


class UnavailableService(BaseModel):
    service = {"id": config.service_id, "name": config.service_name}
    status = {"info": unavailable_service_info}
    error = {"id": 503, "info": "'Service-name' service unavailable"}
    data = {}


class Files(BaseModel):
    fileName: str = Field(...)
    fileBody: str = Field(...)
    fileType: str = Field(...)

    @validator("fileBody")
    def validate_size_in_file(cls, string_base_64):
        # get the approximate size of the original file that was encoded
        size_file = len(string_base_64) - 814 / 1.37

        # validated 2MB max
        if size_file > 2000000:
            raise ValueError("Has exceeded the set size of 2 MB")
        return string_base_64


class CommonRequestBody(BaseModel):
    phoneNumber: str = Field(None)
    chargeAccepted: bool = Field(None)
    comments: str = Field(None)
    files: list[Files] = Field(None)
