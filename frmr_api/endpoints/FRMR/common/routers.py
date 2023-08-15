from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from frmr_api.endpoints.FRMR.common import schemas as CommonSchemas
from frmr_api.endpoints.FRMR.common.services import get_common, create_common
from frmr_api.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from frmr_api.utils.jwtHandler import authorize_jwt_token

router = APIRouter(
    tags=['PERSON'],
    prefix='/person'
)


@router.get('/common')
async def get(db: Session = Depends(get_db),
              params: PersonOid = Depends(),
              token: str = Depends(authorize_jwt_token)) -> CommonSchemas.EducationCommon:
    return get_common(params=params, db=db)


@router.post('/common')
async def post(data: CommonSchemas.EducationCommon, db: Session = Depends(get_db),
               params: PersonOid = Depends(),
               token: str = Depends(authorize_jwt_token)) -> CommonSchemas.EducationCommon:
    return create_common(data=data, oid=params.oid, db=db)
