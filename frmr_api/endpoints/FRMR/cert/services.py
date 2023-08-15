from fastapi import HTTPException
from starlette import status

from frmr_api.endpoints.FRMR.cert import schemas as CertSchemas, models as CertModels
from frmr_api.endpoints.FRMR.person.models import Person
from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from sqlalchemy.orm import Session
from sqlalchemy import column


def create_cert(data: list[CertSchemas.EducationCert], oid: str, db: Session, commit: bool = True):
    person = db.query(Person).filter(column("oid") == oid).first()
    if person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")

    person.educationCert.clear()
    person.educationCert.extend([CertModels.EducationCert(**certData.dict()) for certData in data])

    if commit:
        db.commit()
    return person


def get_cert(params: PersonOid, db: Session):
    person = db.query(Person).filter(column("oid") == params.oid).first()
    if person:
        return CertSchemas.EducationCerts.from_orm(person)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
