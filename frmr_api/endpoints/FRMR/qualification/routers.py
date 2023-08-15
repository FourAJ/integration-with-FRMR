from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from frmr_api.endpoints.FRMR.qualification import schemas as QualificationSchemas
from frmr_api.endpoints.FRMR.qualification.services import get_qualification, create_qualification
from frmr_api.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from frmr_api.utils.jwtHandler import authorize_jwt_token

router = APIRouter(
    tags=['PERSON'],
    prefix='/person'
)


@router.get('/qualification')
async def get(db: Session = Depends(get_db),
              params: PersonOid = Depends(),
              token: str = Depends(authorize_jwt_token)) -> QualificationSchemas.Qualifications:
    return get_qualification(params=params, db=db)


@router.post('/qualification')
async def post(data: list[QualificationSchemas.Qualification], db: Session = Depends(get_db),
               params: PersonOid = Depends(),
               token: str = Depends(authorize_jwt_token)) -> QualificationSchemas.Qualifications:
    return create_qualification(data=data, oid=params.oid, db=db)
