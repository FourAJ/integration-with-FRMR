from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from frmr_api.endpoints.FRMR.organization import schemas as OrgSchemas
from frmr_api.endpoints.FRMR.organization.services import get_org, create_org
from frmr_api.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from frmr_api.utils.jwtHandler import authorize_jwt_token

router = APIRouter(
    tags=['PERSON'],
    prefix='/person'
)


@router.get('/organization')
async def get(db: Session = Depends(get_db),
              params: PersonOid = Depends(), token: str = Depends(authorize_jwt_token)) -> OrgSchemas.Organizations:
    return get_org(params=params, db=db)


@router.post('/organization')
async def post(data: list[OrgSchemas.Organization], db: Session = Depends(get_db),
               params: PersonOid = Depends(), token: str = Depends(authorize_jwt_token)) -> OrgSchemas.Organizations:
    return create_org(data=data, oid=params.oid, db=db)
