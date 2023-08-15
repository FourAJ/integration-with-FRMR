from fastapi import HTTPException
from starlette import status

from frmr_api.endpoints.FRMR.common import schemas as CommonSchemas, models as CommonModels
from frmr_api.endpoints.FRMR.person.models import Person
from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from sqlalchemy.orm import Session
from sqlalchemy import column

from frmr_api.utils.modelHandler import getDatabaseObj


def create_common(data: CommonSchemas.EducationCommon, oid: str, db: Session, commit: bool = True):
    person = db.query(Person).filter(column("oid") == oid).first()
    if person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")

    common = getDatabaseObj(model=CommonModels.EducationCommon, filter_name='commonId', filter_param=data.commonId,
                            data=data.dict(exclude={"profCourseSet"}), db=db)

    common.profCourseSet.clear()
    common.profCourseSet.extend([CommonModels.ProfCourseSet(**courseData.dict()) for courseData in data.profCourseSet])

    common.persons.append(person)

    if commit:
        db.commit()
    return common


def get_common(params: PersonOid, db: Session):
    person = db.query(Person).filter(column("oid") == params.oid).first()
    if person:
        return CommonSchemas.EducationCommon.from_orm(person.educationCommon)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
