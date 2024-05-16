from pydantic import BaseModel
from typing import List

from config import Settings

config = Settings()


class GeneralData(BaseModel):
    matricula: str = None
    nombre: str = None
    campus: str = None
    nivel: str = None
    clave_prog: str = None
    programa: str = None
    turno: str = None
    grupo: str = None
    celular: str = None
    incorporante: str = None
    cred_cursados: int = None
    cred_prog: int = None
    periodicidad: str = None


class GeneralDataResponse(BaseModel):
    data: GeneralData
    error: dict = {}
    partialResponse: dict = {}
    service: dict = {"id": config.service_id, "name": config.service_name}
    status: dict = {"id": 200, "info": "Reenrollment data has been sent correctly"}