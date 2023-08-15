from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from frmr_api.endpoints.FRMR.card import schemas as CardSchemas
from frmr_api.endpoints.FRMR.card.services import get_card, create_card
from frmr_api.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from frmr_api.utils.jwtHandler import authorize_jwt_token

router = APIRouter(
    tags=['PERSON'],
    prefix='/person'
)


@router.get('/card')
async def get(db: Session = Depends(get_db),
              params: PersonOid = Depends(), token: str = Depends(authorize_jwt_token)) -> CardSchemas.Cards:
    return get_card(params=params, db=db)


@router.post('/card')
async def post(data: list[CardSchemas.Card], db: Session = Depends(get_db),
               params: PersonOid = Depends(), token: str = Depends(authorize_jwt_token)) -> CardSchemas.Cards:
    return create_card(data=data, oid=params.oid, db=db)
