from typing import List
from pydantic import BaseModel
from pydantic.validators import datetime


class ProfCourseSet(BaseModel):
    docDate: datetime
    profCourseId: int
    profCourseName: str

    class Config:
        orm_mode = True


class EducationCommon(BaseModel):
    commonId: str
    institution: str
    docSerial: str
    docNumber: str
    docDate: datetime
    profCourseSet: List[ProfCourseSet]

    class Config:
        orm_mode = True
        from_orm = True
