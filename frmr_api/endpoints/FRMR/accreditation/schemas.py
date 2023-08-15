from typing import List
from pydantic import BaseModel
from pydantic.validators import datetime


class Document(BaseModel):
    documentId: int
    serial: str
    number: str

    class Config:
        orm_mode = True


class Key(BaseModel):
    snils: str
    document: Document

    class Config:
        orm_mode = True


class Secretaries(BaseModel):
    snils: str
    document: Document

    class Config:
        orm_mode = True


class Procedure(BaseModel):
    registryNumber: str
    secretaries: List[Secretaries]
    key: List[Key]
    applicationId: str
    firstName: str
    patronymic: str
    lastName: str
    accreditationKindId: int
    accreditationKind: str
    postId: int
    post: str
    specId: int
    spec: str
    mpSpecId: int
    profStandardId: int
    profStandard: str
    institutionId: int
    institution: str
    accreditationActivityKind: str
    passed: bool
    excluded: bool
    passDate: datetime
    endDate: datetime
    protocolDate: datetime
    protocolNumber: str
    educationLevel: int

    class Config:
        orm_mode = True


class Accreditation(BaseModel):
    id: str
    protocolDate: datetime
    protocolNumber: int
    docSerial: str
    docNumber: str
    regNumber: str
    accreditationProcedures: List[Procedure]

    class Config:
        orm_mode = True
        from_orm = True
