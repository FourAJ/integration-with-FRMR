from fastapi import HTTPException
from starlette import status

from frmr_api.endpoints.FRMR.prof import schemas as ProfSchemas, models as ProfModels
from frmr_api.endpoints.FRMR.person.models import Person
from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from sqlalchemy.orm import Session
from sqlalchemy import column

from frmr_api.utils.modelHandler import getDatabaseObj


def create_prof(data: list[ProfSchemas.EducationProf], oid: str, db: Session, commit: bool = True):
    person = db.query(Person).filter(column("oid") == oid).first()
    if person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")

    profList = []
    for prof in data:
        educationType = getDatabaseObj(model=ProfModels.EducationType, filter_name='code',
                                       filter_param=prof.educationTypeId.code,
                                       data=prof.educationTypeId.dict(), db=db)

        personProf = getDatabaseObj(model=ProfModels.EducationProf, filter_name='profId',
                                    filter_param=prof.profId,
                                    data=prof.dict(exclude={"educationTypeId", "courses"}), db=db)

        educationType.educationProf.append(personProf)

        personProf.courses.clear()
        personProf.courses.extend([ProfModels.Course(**CourseData.dict()) for CourseData in prof.courses])

        profList.append(personProf)

    db.add_all(profList)
    person.educationProf.clear()
    person.educationProf.extend(profList)

    if commit:
        db.commit()
    return person


def get_prof(params: PersonOid, db: Session):
    person = db.query(Person).filter(column("oid") == params.oid).first()
    if person:
        return ProfSchemas.EducationProfs.from_orm(person)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
