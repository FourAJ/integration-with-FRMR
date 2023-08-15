from typing import List
from pydantic import BaseModel
from pydantic.validators import datetime


class Ext(BaseModel):
    extId: str
    profEducationKindId: int
    profEducationKindName: str
    institutionId: int
    institutionName: str
    hoursCount: int
    theme: str
    docSerial: str
    docNumber: str
    docDate: datetime
    specId: int
    specName: str

    class Config:
        orm_mode = True


class Exts(BaseModel):
    personExt: List[Ext]

    class Config:
        orm_mode = True
        from_orm = True
