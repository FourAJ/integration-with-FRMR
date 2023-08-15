from fastapi import HTTPException
from starlette import status

from frmr_api.endpoints.FRMR.ext import schemas as ExtSchemas, models as ExtModels
from frmr_api.endpoints.FRMR.person.models import Person
from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from sqlalchemy.orm import Session
from sqlalchemy import column


def create_ext(data: list[ExtSchemas.Ext], oid: str, db: Session, commit: bool = True):
    person = db.query(Person).filter(column("oid") == oid).first()
    if person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")

    person.personExt.clear()
    person.personExt.extend([ExtModels.Ext(**certData.dict()) for certData in data])

    if commit:
        db.commit()
    return person


def get_ext(params: PersonOid, db: Session):
    person = db.query(Person).filter(column("oid") == params.oid).first()
    if person:
        return ExtSchemas.Exts.from_orm(person)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
