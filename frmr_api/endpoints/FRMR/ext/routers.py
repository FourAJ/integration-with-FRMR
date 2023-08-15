from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from frmr_api.endpoints.FRMR.ext import schemas as ExtSchemas
from frmr_api.endpoints.FRMR.ext.services import get_ext, create_ext
from frmr_api.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from frmr_api.utils.jwtHandler import authorize_jwt_token

router = APIRouter(
    tags=['PERSON'],
    prefix='/person'
)


@router.get('/ext')
async def get(db: Session = Depends(get_db),
              params: PersonOid = Depends(), token: str = Depends(authorize_jwt_token)) -> ExtSchemas.Exts:
    return get_ext(params=params, db=db)


@router.post('/ext')
async def post(data: list[ExtSchemas.Ext], db: Session = Depends(get_db),
               params: PersonOid = Depends(), token: str = Depends(authorize_jwt_token)) -> ExtSchemas.Exts:
    return create_ext(data=data, oid=params.oid, db=db)
