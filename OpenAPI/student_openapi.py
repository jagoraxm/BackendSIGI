from pydantic import BaseModel, Field, validator


class ReenrollmentDataRB(BaseModel):
    studentEnrollmentNumber: str = None
    school: str = None
