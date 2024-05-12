from pydantic import BaseModel
from typing import List, Optional

from config import Settings


config = Settings()


class ReportCard(BaseModel):
    crn: str = None
    matricula: str = None
    alumno: str = None
    campus: str = None
    programa: str = None
    ciclo: str = None
    bloque: str = None
    grupo: str = None
    num_mat: int = None
    clave: str = None
    asignatura: str = None
    parcial1: float = None
    parcial2: float = None
    parcial3: float = None
    exam_final: Optional[float] = None
    prom_p1: float = None
    prom_p2: float = None
    prom_p3: float = None
    prom_exfinal: Optional[float] = None
    prom_f: float = None
    faltasp1: int = None
    faltasp2: int = None
    faltasp3: int = None
    cal: float = None
    prom_cal: float = None
    calif_final: float = None


class PostReportCardResponse(BaseModel):
    data: list[ReportCard]
    error: dict = {}
    partialResponse: dict = {}
    service: dict = {"id": config.service_id, "name": config.service_name}
    status: dict = {"id": 200, "info": "The records list report card has been send correctly"}


class ReportCardUnam(BaseModel):
    spriden_id: str = None
    matricula_unam: str = None
    alumno: str = None
    campus: str = None
    programa: str = None
    ciclo: str = None
    bloque: str = None
    grupo: str = None
    clave: str = None
    asignatura: str = None
    grado: str = None
    parcial1: float = None
    parcial2: float = None
    parcial3: float = None
    parcial4: float = None
    prim_vuelta: str = None
    seg_vuelta: str = None
    final: float = None
    conducta1: float = None
    conducta2: float = None
    conducta3: float = None
    conducta4: float = None
    conducta_final: float = None
    faltasp1: int = None
    faltasp2: int = None
    faltasp3: int = None
    faltasp4: int = None
    cal: float = None
    calif_final: float = None
    totfal: float = None
    cp: str = None
    aut: str = None
    observaciones: str = None
    prom_4p: float = None


class PostReportCardUnamResponse(BaseModel):
    data: list[ReportCardUnam]
    error: dict = {}
    partialResponse: dict = {}
    service: dict = {"id": config.service_id, "name": config.service_name}
    status: dict = {"id": 200, "info": "The records list report card unam has been send correctly"}


class AcademicHistory(BaseModel):
    orden_plan: int = None
    clave1: str = None
    clave: str = None
    materia: str = None
    calificacion: str = None
    creditos: int = None
    area: str = None
    shrtckn_term_code: str = None
    periodo: str = None
    tipo: str = None
    matricula: str = None
    alumno: str = None
    programa: str = None
    creditos_totales: int = None
    nivel: str = None
    smrprle_levl_code: str = None
    stvlevl_desc: str = None
    creditos_cubiertos: int = None
    aprobadas: int = None
    no_aprobadas: int = None
    promedio_grado: float = None
    promedio: float = None
    rvoe: str = None
    fecha: str = None
    dtes: str = None
    detalles_legales: str = None
    grado: str = None
    plantel: str = None


class PostAcademicHistoryResponse(BaseModel):
    data: list[AcademicHistory]
    error: dict = {}
    partialResponse: dict = {}
    service: dict = {"id": config.service_id, "name": config.service_name}
    status: dict = {"id": 200, "info": "The records list academic history has been send correctly"}
