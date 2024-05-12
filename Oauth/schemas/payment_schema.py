from datetime import datetime

from pydantic import BaseModel
from typing import List

from config import Settings

config = Settings()


class Debts(BaseModel):
    periodo: str = None
    periodo_desc: str = None
    transaccion: int = None
    cod_det: str = None
    descripcion: str = None
    importe: float = None
    descuentos: float = None
    pagos_aplicados: float = None
    saldo: float = None
    fecha_venc: str = None
    ficha: str = None
    pagos_sin_aplicar: float = None
    tipo_concepto: str = None
    desc_pago_com: str = None
    desc_pronto_pago: str = None


class DebtsResponse(BaseModel):
    data: list[Debts]
    error: dict = {}
    partialResponse: dict = {}
    service: dict = {"id": config.service_id, "name": config.service_name}
    status: dict = {"id": 200, "info": "The records list debts has been send correctly"}


class Sequence(BaseModel):
    sequence: int = None


class SequenceResponse(BaseModel):
    data: str
    error: dict = {}
    partialResponse: dict = {}
    service: dict = {"id": config.service_id, "name": config.service_name}
    status: dict = {"id": 200, "info": "The sequence number has been send correctly"}


class InsertBankResponse(BaseModel):
    data: int
    error: dict = {}
    partialResponse: dict = {}
    service: dict = {"id": config.service_id, "name": config.service_name}
    status: dict = {"id": 201, "info": "The data has been inserted correctly"}


class GenerateSheet(BaseModel):
    # fecha_ven: str
    # fecha_venc: str
    # importe_ficha: float
    # tran: str
    # var_id_persona: str
    # var_referencia: str
    # prm_importe_entero: str
    # prm_importe_decimal: str
    # ref_banbajio: str
    # var_id_persona_: str
    # prm_importe_entero_: str
    # prm_importe_decimal_: str
    # ref_sant_bancomer: str
    # ref_oxxo: str

    pidm: int = None
    amount: float = None
    due_date: str = None
    ref_number: int = None
    activity_date: str = None
    status: str = None
    user: str = None
    ref_santander: str = None
    ref_banbajio: str = None
    ref_oxxo: str = None
    add: str = None
    add_one: str = None
    add_two: str = None
    add_three: str = None


class GenerateSheetResponse(BaseModel):
    data: GenerateSheet
    error: dict = {}
    partialResponse: dict = {}
    service: dict = {"id": config.service_id, "name": config.service_name}
    status: dict = {"id": 201, "info": "The sheet bank references sent correctly"}


class Reference(BaseModel):
    tzrbank_amount: str
    tzrbank_ref_banbajio: str
    tzrbank_ref_santander: str
    tzrbank_ref_oxxo: str
    tzrbank_due_date: str


class ReferenceResponse(BaseModel):
    data: list[Reference]
    error: dict = {}
    partialResponse: dict = {}
    service: dict = {"id": config.service_id, "name": config.service_name}
    status: dict = {"id": 200, "info": "The references has been send correctly"}


class PaymentSheet(BaseModel):
    secuencia: int = None
    monto: float = None
    fecha_vencimiento: str = None


class ListPaymentSheetResponse(BaseModel):
    data: list[PaymentSheet]
    error: dict = {}
    partialResponse: dict = {}
    service: dict = {"id": config.service_id, "name": config.service_name}
    status: dict = {"id": 200, "info": "The list payment sheet has been send correctly"}



