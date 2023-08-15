from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from frmr_api.endpoints.FRMR.prof import schemas as ProfSchemas
from frmr_api.endpoints.FRMR.prof.services import create_prof, get_prof
from frmr_api.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from frmr_api.utils.jwtHandler import authorize_jwt_token

router = APIRouter(
    tags=['PERSON'],
    prefix='/person'
)


@router.get('/prof')
async def get(db: Session = Depends(get_db),
              params: PersonOid = Depends(), token: str = Depends(authorize_jwt_token)) -> ProfSchemas.EducationProfs:
    return get_prof(params=params, db=db)


@router.post('/prof')
async def post(data: list[ProfSchemas.EducationProf], db: Session = Depends(get_db),
               params: PersonOid = Depends(), token: str = Depends(authorize_jwt_token)) -> ProfSchemas.EducationProfs:
    return create_prof(data=data, oid=params.oid, db=db)
