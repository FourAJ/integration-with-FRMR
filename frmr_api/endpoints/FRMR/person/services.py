from fastapi import HTTPException
from starlette import status

from frmr_api.endpoints.FRMR.accreditation.services import create_accreditation
from frmr_api.endpoints.FRMR.card.services import create_card
from frmr_api.endpoints.FRMR.cert.services import create_cert
from frmr_api.endpoints.FRMR.common.services import create_common
from frmr_api.endpoints.FRMR.ext.services import create_ext
from frmr_api.endpoints.FRMR.nomination.services import create_nomination
from frmr_api.endpoints.FRMR.organization.services import create_org
from frmr_api.endpoints.FRMR.person import schemas as PersonSchemas, models as PersonModels
from sqlalchemy.orm import Session
from sqlalchemy import column

from frmr_api.endpoints.FRMR.postgraduate.services import create_postgraduate
from frmr_api.endpoints.FRMR.prof.services import create_prof
from frmr_api.endpoints.FRMR.qualification.services import create_qualification
from frmr_api.utils.modelHandler import getDatabaseObj


def create_person(data: PersonSchemas.Person, mo: str, db: Session, commit: bool = True):
    citizenShip = getDatabaseObj(model=PersonModels.CitizenShip, filter_name='code', filter_param=data.citizenShipId.code,
                                 data=data.citizenShipId.dict(), db=db)

    oksm = getDatabaseObj(model=PersonModels.Oksm, filter_name='code', filter_param=data.oksmId.code,
                          data=data.oksmId.dict(), db=db)

    person = getDatabaseObj(model=PersonModels.Person, filter_name='oid', filter_param=data.oid,
                            data=data.dict(exclude={"citizenShipId", "oksmId", "documents", "addresses"}), db=db)
    person.mo = mo

    citizenShip.persons.append(person)
    oksm.persons.append(person)

    person.documents.clear()
    person.documents.extend([PersonModels.Document(**documentData.dict()) for documentData in data.documents])

    addressesList = []
    for adr in data.addresses:
        address = getDatabaseObj(model=PersonModels.Address, filter_name='addressId',
                                 filter_param=adr.dict(exclude={"address"})['addressId'],
                                 data=adr.dict(exclude={"address"}), db=db)

        subAddress = getDatabaseObj(model=PersonModels.SubAddress, filter_name='GARguid',
                                    filter_param=adr.address.dict()["GARguid"],
                                    data=adr.address.dict(), db=db)

        subAddress.addresses.append(address)
        addressesList.append(address)

    db.add_all(addressesList)
    person.addresses.clear()
    person.addresses.extend(addressesList)

    if commit:
        db.commit()

    return person


def create_person_list(data: list, mo: str, db: Session):
    personList = []
    for person in data:
        newPerson = create_person(data=PersonSchemas.Person(**person.dict()), mo=mo, db=db, commit=False)
        personList.append(newPerson)

    db.add_all(personList)
    db.commit()
    return [PersonSchemas.Person.from_orm(person) for person in personList]


def get_person(db: Session, oid: str):
    person = db.query(PersonModels.Person).filter(column('oid') == oid).first()
    if person:
        return PersonSchemas.Person.from_orm(person)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")


def get_person_full(db: Session, oid: str):
    person = db.query(PersonModels.Person).filter(column('oid') == oid).first()
    if person:
        return PersonSchemas.PersonFull.from_orm(person)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")


def get_person_list(db: Session, mo: str, offset: int, limit: int):
    offset = offset if offset is not None else 0

    limit = limit if limit is not None else 100
    limit = min(limit, 100)

    query = db.query(PersonModels.Person).filter(column("mo") == mo)
    query = query.offset(offset).limit(limit)
    person_list = query.all()
    return [PersonSchemas.Person.from_orm(person) for person in person_list]


def create_person_full(data: PersonSchemas.PersonFull, mo: str, db: Session):
    person = create_person(data=PersonSchemas.Person(**data.dict()), mo=mo, db=db, commit=False)

    create_accreditation(data=data.personAccreditation, oid=data.oid, db=db, commit=False)
    create_card(data=data.personCard, oid=data.oid, db=db, commit=False)
    create_cert(data=data.educationCert, oid=data.oid, db=db, commit=False)
    create_common(data=data.educationCommon, oid=data.oid, db=db, commit=False)
    create_ext(data=data.personExt, oid=data.oid, db=db, commit=False)
    create_nomination(data=data.personNomination, oid=data.oid, db=db, commit=False)
    create_org(data=data.personOrganization, oid=data.oid, db=db, commit=False)
    create_postgraduate(data=data.personPostgraduate, oid=data.oid, db=db, commit=False)
    create_prof(data=data.educationProf, oid=data.oid, db=db, commit=False)
    create_qualification(data=data.personQualification, oid=data.oid, db=db, commit=False)

    db.commit()
    return PersonSchemas.PersonFull.from_orm(person)