from typing import List
from pydantic import BaseModel
from pydantic.validators import datetime


class Dereliction(BaseModel):
    reasonId: int
    beginDate: datetime
    endDate: datetime

    class Config:
        orm_mode = True


class Service(BaseModel):
    code: int
    name: str

    class Config:
        orm_mode = True


class Card(BaseModel):
    id: str
    oid: str
    organization: str
    nrPmuDepartId: str
    nrPmuDepartName: str
    nrPmuDepartHospitalSubdivisionId: str
    nrPmuDepartHospitalSubdivisionName: str
    roomName: str
    roomOid: str
    contractNumber: str
    contractDate: datetime
    serviceNumber: str
    fedPositionId: int
    fedPosition: str
    seniority: int
    services: List[Service]
    positionTypeId: int
    positionTypeName: str
    postId: int
    postName: str
    rate: float
    beginDate: datetime
    endDate: datetime
    endTypeId: int
    fireReasonId: int
    targeted: bool
    temporaryDerelictions: List[Dereliction]

    class Config:
        orm_mode = True


class Cards(BaseModel):
    personCard: List[Card]

    class Config:
        orm_mode = True
        from_orm = True
