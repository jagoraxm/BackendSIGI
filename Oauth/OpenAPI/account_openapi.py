from pydantic import BaseModel, Field, validator


class AccountStatusRB(BaseModel):
    studentEnrollmentNumber: str = None
    school: str = None
