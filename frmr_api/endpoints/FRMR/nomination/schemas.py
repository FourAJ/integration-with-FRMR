from typing import List
from pydantic import BaseModel
from pydantic.validators import datetime


class Nomination(BaseModel):
    nominationId: int
    nomNumber: str
    nomDate: datetime
    entityId: str

    class Config:
        orm_mode = True


class Nominations(BaseModel):
    personNomination: List[Nomination]

    class Config:
        orm_mode = True
        from_orm = True
