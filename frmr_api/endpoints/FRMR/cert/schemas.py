from typing import List
from pydantic import BaseModel
from pydantic.validators import datetime


class EducationCert(BaseModel):
    certId: str
    institutionId: int
    institutionName: str
    certSerial: str
    certNumber: str
    examDate: datetime
    passDate: datetime
    endDate: datetime
    specId: int
    specName: str

    class Config:
        orm_mode = True


class EducationCerts(BaseModel):
    educationCert: List[EducationCert]

    class Config:
        orm_mode = True
        from_orm = True
