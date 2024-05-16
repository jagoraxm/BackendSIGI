from pydantic import BaseModel
from typing import List

from config import Settings

config = Settings()


class AccountStatus(BaseModel):
    trans_cargo: int = None
    periodo_cargo: str = None
    mes: str = None
    desc_concepto_cargo: str = None
    importe: float = None
    beca: float = None
    pagos: float = None
    becas: float = None
    cargos: float = None
    saldo_final: float = None
    fecha_vencimiento_cargo: str = None
    saldo_pendiente: float = None
    tipo: str = None
    iden: str = None
    nombre: str = None


class PostAccountStatusResponse(BaseModel):
    data: list[AccountStatus]
    error: dict = {}
    partialResponse: dict = {}
    service: dict = {"id": config.service_id, "name": config.service_name}
    status: dict = {"id": 200, "info": "The records list account status has been send correctly"}
