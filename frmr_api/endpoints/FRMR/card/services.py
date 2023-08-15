from fastapi import HTTPException
from starlette import status

from frmr_api.endpoints.FRMR.card import schemas as CardSchemas, models as CardModels
from frmr_api.endpoints.FRMR.person.models import Person
from frmr_api.endpoints.FRMR.person.schemas import PersonOid
from sqlalchemy.orm import Session
from sqlalchemy import column

from frmr_api.utils.modelHandler import getDatabaseObj


def create_card(data: list[CardSchemas.Card], oid: str, db: Session, commit: bool = True):
    person = db.query(Person).filter(column("oid") == oid).first()
    if person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    cardList = []
    for cardSchema in data:
        card = getDatabaseObj(model=CardModels.Card, filter_name='id', filter_param=cardSchema.id,
                              data=cardSchema.dict(exclude={"temporaryDerelictions", "services"}), db=db)

        card.services.clear()
        card.services.extend([CardModels.Service(**serviceData.dict()) for serviceData in cardSchema.services])

        card.temporaryDerelictions.clear()
        card.temporaryDerelictions.extend(
            [CardModels.Dereliction(**tempData.dict()) for tempData in cardSchema.temporaryDerelictions])

        cardList.append(card)

    db.add_all(cardList)
    person.personCard.clear()
    person.personCard.extend(cardList)

    if commit:
        db.commit()
    return person


def get_card(params: PersonOid, db: Session):
    person = db.query(Person).filter(column("oid") == params.oid).first()
    if person:
        return CardSchemas.Cards.from_orm(person)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
