from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from frmr_api.endpoints.FRMR.accreditation import schemas as AccreditationSchemas
from frmr_api.endpoints.FRMR.accreditation.services import create_accreditation, get_accreditation
from frmr_api.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from frmr_api.utils.jwtHandler import authorize_jwt_token

router = APIRouter(
    tags=['PERSON'],
    prefix='/person'
)


@router.get('/accreditation')
async def get(db: Session = Depends(get_db),
              params: PersonOid = Depends(),
              token: str = Depends(authorize_jwt_token)) -> AccreditationSchemas.Accreditation:
    return get_accreditation(params=params, db=db)


@router.post('/accreditation')
async def post(data: AccreditationSchemas.Accreditation, db: Session = Depends(get_db),
               params: PersonOid = Depends(),
               token: str = Depends(authorize_jwt_token)) -> AccreditationSchemas.Accreditation:
    return create_accreditation(data=data, oid=params.oid, db=db)
