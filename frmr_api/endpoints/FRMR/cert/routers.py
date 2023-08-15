from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from frmr_api.endpoints.FRMR.cert import schemas as CertSchemas
from frmr_api.endpoints.FRMR.cert.services import create_cert, get_cert
from frmr_api.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from frmr_api.utils.jwtHandler import authorize_jwt_token

router = APIRouter(
    tags=['PERSON'],
    prefix='/person'
)


@router.get('/cert')
async def get(db: Session = Depends(get_db),
              params: PersonOid = Depends(), token: str = Depends(authorize_jwt_token)) -> CertSchemas.EducationCerts:
    return get_cert(params=params, db=db)


@router.post('/cert')
async def post(data: list[CertSchemas.EducationCert], db: Session = Depends(get_db),
               params: PersonOid = Depends(), token: str = Depends(authorize_jwt_token)) -> CertSchemas.EducationCerts:
    return create_cert(data=data, oid=params.oid, db=db)
