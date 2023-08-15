from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from frmr_api.database.database import Base
from frmr_api.endpoints.FRMR.cert.models import EducationCert
from frmr_api.endpoints.FRMR.organization.models import Organization
from frmr_api.endpoints.FRMR.nomination.models import Nomination
from frmr_api.endpoints.FRMR.qualification.models import Qualification
from frmr_api.endpoints.FRMR.ext.models import Ext
from frmr_api.endpoints.FRMR.postgraduate.models import Postgraduate
from frmr_api.endpoints.FRMR.common.models import EducationCommon
from frmr_api.endpoints.FRMR.card.models import Card
from frmr_api.endpoints.FRMR.accreditation.models import Accreditation
from frmr_api.endpoints.FRMR.prof.models import EducationProf


class CitizenShip(Base):
    __tablename__ = 'citizenship'

    code = Column(Integer, primary_key=True)
    name = Column(String)

    persons = relationship('Person', back_populates='citizenShipId')


class Oksm(Base):
    __tablename__ = 'oksm'

    code = Column(Integer, primary_key=True)
    name = Column(String)

    persons = relationship('Person', back_populates='oksmId')


class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True, autoincrement=True)

    documentId = Column(Integer)
    serial = Column(String)
    number = Column(String)
    passDate = Column(DateTime)
    passOrg = Column(String)
    codeOrg = Column(String)

    person_oid = Column(String, ForeignKey('person.oid', ondelete='CASCADE'))
    person = relationship('Person', back_populates='documents')


class Address(Base):  # Address
    __tablename__ = 'address'

    addressId = Column(String, primary_key=True)
    regDate = Column(DateTime)
    addressTypeId = Column(Integer)

    person_oid = Column(String, ForeignKey('person.oid', ondelete='CASCADE'))
    person = relationship('Person', back_populates='addresses')

    addressGuid = Column(String, ForeignKey('subAddress.GARguid'))
    address = relationship('SubAddress', back_populates='addresses', lazy='joined')


class SubAddress(Base):  # sub Address
    __tablename__ = 'subAddress'

    GARguid = Column(String, primary_key=True)
    aoidArea = Column(String)
    aoidStreet = Column(String)
    houseid = Column(String)
    region = Column(Integer)
    areaName = Column(String)
    prefixArea = Column(String)
    streetName = Column(String)
    prefixStreet = Column(String)
    house = Column(String)
    building = Column(String)
    struct = Column(String)
    flat = Column(String)

    addresses = relationship('Address', back_populates='address')


class Person(Base):
    __tablename__ = 'person'

    oid = Column(String, primary_key=True, index=True)
    mo = Column(String)
    mr = Column(Boolean)
    student = Column(Boolean)
    snils = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    patronymic = Column(String)
    gender = Column(Integer)
    birthDate = Column(DateTime)
    inn = Column(String)

    citizenShip = Column(Integer, ForeignKey('citizenship.code'))
    citizenShipId = relationship('CitizenShip', back_populates='persons', lazy='joined')

    oksm = Column(Integer, ForeignKey('oksm.code'))
    oksmId = relationship('Oksm', back_populates='persons', lazy='joined')

    militaryRelationId = Column(Integer)
    phone = Column(String)
    email = Column(String)
    isDisabled = Column(Boolean)
    disabledGroupId = Column(Integer)
    disabledGroupName = Column(String)
    disabledDate = Column(DateTime)
    covid19 = Column(Boolean)

    documents = relationship('Document', back_populates='person', cascade="all, delete-orphan")
    addresses = relationship('Address', back_populates='person', cascade="all, delete-orphan")
    educationCert = relationship('EducationCert', back_populates='person', cascade="all, delete-orphan")
    personOrganization = relationship('Organization', back_populates='person', cascade="all, delete-orphan")
    personNomination = relationship('Nomination', back_populates='person', cascade="all, delete-orphan")
    personQualification = relationship('Qualification', back_populates='person', cascade="all, delete-orphan")
    personExt = relationship('Ext', back_populates='person', cascade="all, delete-orphan")
    personPostgraduate = relationship('Postgraduate', back_populates='person', cascade="all, delete-orphan")
    educationProf = relationship('EducationProf', back_populates='person', cascade="all, delete-orphan")
    personCard = relationship('Card', back_populates='person', cascade="all, delete-orphan")

    personAccreditationId = Column(String, ForeignKey('accreditation.id'))
    personAccreditation = relationship('Accreditation', back_populates='persons', lazy='joined')

    educationCommonId = Column(String, ForeignKey('common.commonId'))
    educationCommon = relationship('EducationCommon', back_populates='persons', lazy='joined')
