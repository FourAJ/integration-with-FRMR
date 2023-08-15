from typing import List
from pydantic import BaseModel
from pydantic.validators import datetime


class Qualification(BaseModel):
    qualificationId: str
    qualifyCategoryId: int
    qualifyCategoryName: str
    beginDate: datetime
    endDate: datetime
    specId: int
    specName: str
    fedPostId: int
    fedPostName: str
    postId: int
    postName: str

    class Config:
        orm_mode = True


class Qualifications(BaseModel):
    personQualification: List[Qualification]

    class Config:
        orm_mode = True
        from_orm = True
