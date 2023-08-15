from typing import List
from pydantic import BaseModel
from pydantic.validators import datetime


class Postgraduate(BaseModel):
    postgraduateId: str
    isDuplicate: bool
    educPlace: int
    educationStageId: int
    educationStageName: str
    isStudying: bool
    beginYear: int
    docSerial: str
    docNumber: str
    docDate: datetime
    institutionId: int
    institutionName: str
    academicDegreeId: int
    academicDegreeName: str
    scienceBranchId: int
    scienceBranchName: str
    specId: int
    specName: str
    doctSpecId: int
    doctSpecName: str
    additionSpecId: int
    additionSpecName: str
    isTargeted: bool
    targetedRegionId: int
    dutyMonthsPeriod: int
    dutyYearsPeriod: int
    isTargetTerminated: bool
    terminationReasonId: int
    dutyInfo: str
    oksmId: int
    oksmName: str
    unionRepublicId: int
    unionRepublicName: str
    foreignInstitution: str
    hasForeignCert: int
    foreignCertSerial: str
    foreignCertNumber: str
    foreignCertDate: datetime

    class Config:
        orm_mode = True


class Postgraduates(BaseModel):
    personPostgraduate: List[Postgraduate]

    class Config:
        orm_mode = True
        from_orm = True
