from typing import List, Optional
from pydantic import BaseModel
from pydantic.validators import datetime

from frmr_api.endpoints.FRMR.accreditation.schemas import Accreditation
from frmr_api.endpoints.FRMR.card.schemas import Card
from frmr_api.endpoints.FRMR.cert.schemas import EducationCert
from frmr_api.endpoints.FRMR.common.schemas import EducationCommon
from frmr_api.endpoints.FRMR.ext.schemas import Ext
from frmr_api.endpoints.FRMR.nomination.schemas import Nomination
from frmr_api.endpoints.FRMR.organization.schemas import Organization
from frmr_api.endpoints.FRMR.postgraduate.schemas import Postgraduate
from frmr_api.endpoints.FRMR.prof.schemas import EducationProf
from frmr_api.endpoints.FRMR.qualification.schemas import Qualification


class CitizenShip(BaseModel):
    code: int
    name: str

    class Config:
        orm_mode = True


class Oksm(BaseModel):
    code: int
    name: str

    class Config:
        orm_mode = True


class Document(BaseModel):
    documentId: int
    serial: str
    number: str
    passDate: datetime
    passOrg: str
    codeOrg: str

    class Config:
        orm_mode = True


class SubAddress(BaseModel):
    GARguid: str
    aoidArea: str
    aoidStreet: str
    houseid: str
    region: int
    areaName: str
    prefixArea: str
    streetName: str
    prefixStreet: str
    house: str
    building: str
    struct: str
    flat: str

    class Config:
        orm_mode = True


class Address(BaseModel):
    addressId: str
    regDate: datetime
    addressTypeId: int
    address: SubAddress

    class Config:
        orm_mode = True


class Person(BaseModel):
    oid: str
    mr: bool
    student: bool
    snils: str
    firstName: str
    lastName: str
    patronymic: str
    gender: int
    birthDate: datetime
    inn: str
    citizenShipId: CitizenShip
    oksmId: Oksm
    militaryRelationId: int
    phone: str
    email: str
    isDisabled: bool
    disabledGroupId: int
    disabledGroupName: str
    disabledDate: datetime
    covid19: bool
    documents: List[Document]
    addresses: List[Address]

    class Config:
        orm_mode = True
        from_orm = True


class PersonFull(Person):
    educationCommon: Optional[EducationCommon]
    educationCert: List[EducationCert]
    personNomination: List[Nomination]
    personOrganization: List[Organization]
    personQualification: List[Qualification]
    personExt: List[Ext]
    personPostgraduate: List[Postgraduate]
    educationProf: List[EducationProf]
    personCard: List[Card]
    personAccreditation: Optional[Accreditation]

    class Config:
        orm_mode = True
        from_orm = True


class PersonOid(BaseModel):
    oid: str


class PersonMo(BaseModel):
    mo: str
