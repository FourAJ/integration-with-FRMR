from typing import List
from pydantic import BaseModel
from pydantic.validators import datetime


class Organization(BaseModel):
    organizationId: str
    beginDate: datetime
    endDate: datetime
    entityId: str

    class Config:
        orm_mode = True


class Organizations(BaseModel):
    personOrganization: List[Organization]

    class Config:
        orm_mode = True
        from_orm = True
