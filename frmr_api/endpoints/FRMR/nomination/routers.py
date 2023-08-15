from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from frmr_api.endpoints.FRMR.nomination import schemas as NominationSchemas
from frmr_api.endpoints.FRMR.nomination.services import get_nomination, create_nomination
from frmr_api.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from frmr_api.utils.jwtHandler import authorize_jwt_token

router = APIRouter(
    tags=['PERSON'],
    prefix='/person'
)


@router.get('/nomination')
async def get(db: Session = Depends(get_db),
              params: PersonOid = Depends(),
              token: str = Depends(authorize_jwt_token)) -> NominationSchemas.Nominations:
    return get_nomination(params=params, db=db)


@router.post('/nomination')
async def post(data: list[NominationSchemas.Nomination], db: Session = Depends(get_db),
               params: PersonOid = Depends(),
               token: str = Depends(authorize_jwt_token)) -> NominationSchemas.Nominations:
    return create_nomination(data=data, oid=params.oid, db=db)
