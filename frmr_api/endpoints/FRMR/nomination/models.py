from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from frmr_api.database.database import Base


class Nomination(Base):
    __tablename__ = 'nomination'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nominationId = Column(Integer)
    nomNumber = Column(String)
    nomDate = Column(DateTime)
    entityId = Column(String)

    person_oid = Column(String, ForeignKey('person.oid', ondelete='CASCADE'))
    person = relationship('Person', back_populates='personNomination')
