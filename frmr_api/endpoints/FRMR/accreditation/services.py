from fastapi import HTTPException
from starlette import status

from frmr_api.endpoints.FRMR.accreditation import schemas as AccreditationSchemas, models as AccreditationModels
from frmr_api.endpoints.FRMR.person.models import Person
from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from sqlalchemy.orm import Session
from sqlalchemy import column

from frmr_api.utils.modelHandler import getDatabaseObj


def create_accreditation(data: AccreditationModels.Accreditation, oid: str, db: Session, commit: bool = True):
    person = db.query(Person).filter(column("oid") == oid).first()
    if person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")

    accreditation = getDatabaseObj(model=AccreditationModels.Accreditation, filter_name='id', filter_param=data.id,
                                   data=data.dict(exclude={"accreditationProcedures"}), db=db)
    accreditation.accreditationProcedures.clear()

    procedureList: list = []
    for procedure in data.accreditationProcedures:
        accreditationProcedure = AccreditationModels.Procedure(**procedure.dict(exclude={"secretaries", "key"}))
        db.add(accreditationProcedure)

        for secretariesItem in procedure.secretaries:
            secretaries = AccreditationModels.Secretaries(**secretariesItem.dict(exclude={"document"}))

            document = AccreditationModels.SecretariesDocument(**secretariesItem.document.dict())
            document.secretaries.append(secretaries)

            accreditationProcedure.secretaries.append(secretaries)

        for keyItem in procedure.key:
            key = AccreditationModels.Key(**keyItem.dict(exclude={"document"}))

            document = AccreditationModels.KeyDocument(**keyItem.document.dict())
            document.key.append(key)

            accreditationProcedure.key.append(key)

        procedureList.append(accreditationProcedure)

    db.add_all(procedureList)
    accreditation.accreditationProcedures.extend(procedureList)
    accreditation.persons.append(person)
    if commit:
        db.commit()
    return accreditation


def get_accreditation(params: PersonOid, db: Session):
    person = db.query(Person).filter(column("oid") == params.oid).first()
    if person:
        return AccreditationSchemas.Accreditation.from_orm(person.personAccreditation)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
