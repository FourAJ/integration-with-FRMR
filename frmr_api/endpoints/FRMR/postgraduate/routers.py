from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from frmr_api.endpoints.FRMR.postgraduate import schemas as PostgraduateSchemas
from frmr_api.endpoints.FRMR.postgraduate.services import get_postgraduate, create_postgraduate
from frmr_api.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from frmr_api.utils.jwtHandler import authorize_jwt_token

router = APIRouter(
    tags=['PERSON'],
    prefix='/person'
)


@router.get('/postgraduate')
async def get(db: Session = Depends(get_db),
              params: PersonOid = Depends(),
              token: str = Depends(authorize_jwt_token)) -> PostgraduateSchemas.Postgraduates:
    return get_postgraduate(params=params, db=db)


@router.post('/postgraduate')
async def post(data: list[PostgraduateSchemas.Postgraduate], db: Session = Depends(get_db),
               params: PersonOid = Depends(),
               token: str = Depends(authorize_jwt_token)) -> PostgraduateSchemas.Postgraduates:
    return create_postgraduate(data=data, oid=params.oid, db=db)
