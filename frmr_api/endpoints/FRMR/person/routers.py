from frmr_api.endpoints.FRMR.person import schemas as PersonSchemas
from frmr_api.endpoints.FRMR.person.services import get_person, create_person, get_person_full, get_person_list, \
    create_person_list, create_person_full
from frmr_api.database.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from frmr_api.utils.jwtHandler import authorize_jwt_token

router = APIRouter(
    tags=['PERSON'],
    prefix='/person',
)


@router.get('/')
async def get(oid: str, db: Session = Depends(get_db),
              token: str = Depends(authorize_jwt_token)) -> PersonSchemas.Person:
    return get_person(oid=oid, db=db)


@router.get('/full')
async def get(oid: str, db: Session = Depends(get_db),
              token: str = Depends(authorize_jwt_token)) -> PersonSchemas.PersonFull:
    return get_person_full(oid=oid, db=db)


@router.get('/list')
async def get(mo: str, offset: int = None,
              limit: int = None, db: Session = Depends(get_db), token: str = Depends(authorize_jwt_token)) -> list[
    PersonSchemas.Person]:
    return get_person_list(mo=mo, offset=offset, limit=limit, db=db)


@router.post('/')
async def post(person: PersonSchemas.Person, params: PersonSchemas.PersonMo = Depends(),
               db: Session = Depends(get_db), token: str = Depends(authorize_jwt_token)) -> PersonSchemas.Person:
    return create_person(data=person, db=db, mo=params.mo)


@router.post('/list')
async def post(person: list[PersonSchemas.Person], params: PersonSchemas.PersonMo = Depends(),
               db: Session = Depends(get_db), token: str = Depends(authorize_jwt_token)) -> list[PersonSchemas.Person]:
    return create_person_list(data=person, db=db, mo=params.mo)


@router.post('/full')
async def post(person: PersonSchemas.PersonFull, params: PersonSchemas.PersonMo = Depends(),
               db: Session = Depends(get_db), token: str = Depends(authorize_jwt_token)) -> PersonSchemas.PersonFull:
    return create_person_full(data=person, db=db, mo=params.mo)
