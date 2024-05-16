from pydantic import BaseModel, Field
from typing import Optional

from config import Settings


config = Settings()


class ResponsePost(BaseModel):
    data = {"user": {}}
    service = {"id": config.service_id, "name": config.service_name}
    error = {}
    partialResponse = {}
    status = {"id": 200, "info": "'Degree' requested successfuly to Salesforce"}


class ResponseGet(BaseModel):
    data = {"recordType": [], "filesLinks": {}, "stepsGuideOnlineDegree": [], "stepsGuideGraduateDegree": []}
    error = {}
    partialResponse = {}
    service = {"id": config.service_id, "name": config.service_name}
    status = {"id": 200, "info": "Degree arrays sent"}


class Files(BaseModel):
    fileName: str = Field(...)
    fileBody: str = Field(...)
    fileType: str = Field(...)


class RequestBody(BaseModel):
    email: str
    password: str

class RequestBodyReg(BaseModel):
    email: str
    password: str
    nombre: str
    apellido: str
    rol: int
    estatus: int