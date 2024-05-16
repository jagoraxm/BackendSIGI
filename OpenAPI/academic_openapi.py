from pydantic import BaseModel, Field, validator


class ReportCardRB(BaseModel):
    studentEnrollmentNumber: str = None
    school: str = None
    period: str = None
    program: str = None


class ReportCardUnamRB(BaseModel):
    studentEnrollmentNumber: str = None
    school: str = None
    period: str = None


class AcademicHistoryRB(BaseModel):
    studentEnrollmentNumber: str = None
    school: str = None
    program: str = None

