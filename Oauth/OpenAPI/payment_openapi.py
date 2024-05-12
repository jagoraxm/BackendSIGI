from pydantic import BaseModel, Field, validator


class DebtsRB(BaseModel):
    studentEnrollmentNumber: str = None
    school: str = None


class SequenceRB(BaseModel):
    school: str = None


class InsertBankRB(BaseModel):
    studentEnrollmentNumber: str
    sequenceNumber: int
    transactionNumber: str
    amount: float
    pc: int
    school: str


class GenerateSheetRB(BaseModel):
    studentEnrollmentNumber: str
    sequenceNumber: int
    school: str


class ReferenceRB(BaseModel):
    school: str
    sequenceNumber: int


class ListPaymentSheetRB(BaseModel):
    studentEnrollmentNumber: str
    school: str

