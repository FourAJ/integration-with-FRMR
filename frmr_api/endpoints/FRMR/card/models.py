from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float, Boolean
from sqlalchemy.orm import relationship
from frmr_api.database.database import Base


class Dereliction(Base):
    __tablename__ = 'dereliction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    reasonId = Column(Integer)
    beginDate = Column(DateTime)
    endDate = Column(DateTime)

    cardId = Column(String, ForeignKey('card.id', ondelete='CASCADE'))
    card = relationship('Card', back_populates='temporaryDerelictions')


class Service(Base):
    __tablename__ = 'service'

    code = Column(Integer, primary_key=True)
    name = Column(String)

    cardId = Column(String, ForeignKey('card.id', ondelete='CASCADE'))
    card = relationship('Card', back_populates='services')


class Card(Base):
    __tablename__ = 'card'

    id = Column(String, primary_key=True)
    oid = Column(String)
    organization = Column(String)
    nrPmuDepartId = Column(String)
    nrPmuDepartName = Column(String)
    nrPmuDepartHospitalSubdivisionId = Column(String)
    nrPmuDepartHospitalSubdivisionName = Column(String)
    roomName = Column(String)
    roomOid = Column(String)
    contractNumber = Column(String)
    contractDate = Column(DateTime)
    serviceNumber = Column(String)
    fedPositionId = Column(Integer)
    fedPosition = Column(String)
    seniority = Column(Integer)
    services = relationship('Service', back_populates='card', cascade="all, delete-orphan")
    positionTypeId = Column(Integer)
    positionTypeName = Column(String)
    postId = Column(Integer)
    postName = Column(String)
    rate = Column(Float)
    beginDate = Column(DateTime)
    endDate = Column(DateTime)
    endTypeId = Column(Integer)
    fireReasonId = Column(Integer)
    targeted = Column(Boolean)
    temporaryDerelictions = relationship('Dereliction', back_populates='card', cascade="all, delete-orphan")

    person_oid = Column(String, ForeignKey('person.oid', ondelete='CASCADE'))
    person = relationship('Person', back_populates='personCard')
