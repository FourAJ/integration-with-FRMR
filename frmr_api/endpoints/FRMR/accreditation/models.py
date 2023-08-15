from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship
from frmr_api.database.database import Base


class Key(Base):
    __tablename__ = 'key'

    id = Column(Integer, primary_key=True, autoincrement=True)
    snils = Column(String)

    documentId = Column(Integer, ForeignKey('keyDocument.id'))
    document = relationship('KeyDocument', back_populates='key', lazy='joined')

    procedureId = Column(String, ForeignKey('procedure.registryNumber', ondelete='CASCADE'))
    procedure = relationship('Procedure', back_populates='key')


class KeyDocument(Base):
    __tablename__ = 'keyDocument'

    id = Column(Integer, primary_key=True, autoincrement=True)

    documentId = Column(Integer)
    serial = Column(String)
    number = Column(String)

    key = relationship('Key', back_populates='document')


class Secretaries(Base):
    __tablename__ = 'secretaries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    snils = Column(String)

    documentId = Column(Integer, ForeignKey('secretariesDocument.id'))
    document = relationship('SecretariesDocument', back_populates='secretaries', lazy='joined')

    procedureId = Column(String, ForeignKey('procedure.registryNumber', ondelete='CASCADE'))
    procedure = relationship('Procedure', back_populates='secretaries')


class SecretariesDocument(Base):
    __tablename__ = 'secretariesDocument'

    id = Column(Integer, primary_key=True, autoincrement=True)

    documentId = Column(Integer)
    serial = Column(String)
    number = Column(String)

    secretaries = relationship('Secretaries', back_populates='document')


class Procedure(Base):
    __tablename__ = 'procedure'

    registryNumber = Column(String, primary_key=True)
    applicationId = Column(String)
    firstName = Column(String)
    patronymic = Column(String)
    lastName = Column(String)
    accreditationKindId = Column(Integer)
    accreditationKind = Column(String)
    postId = Column(Integer)
    post = Column(String)
    specId = Column(Integer)
    spec = Column(String)
    mpSpecId = Column(Integer)
    profStandardId = Column(Integer)
    profStandard = Column(String)
    institutionId = Column(Integer)
    institution = Column(String)
    accreditationActivityKind = Column(String)
    passed = Column(Boolean)
    excluded = Column(Boolean)
    passDate = Column(DateTime)
    endDate = Column(DateTime)
    protocolDate = Column(DateTime)
    protocolNumber = Column(String)
    educationLevel = Column(Integer)

    accreditationId = Column(String, ForeignKey('accreditation.id', ondelete='CASCADE'))

    accreditation = relationship('Accreditation', back_populates='accreditationProcedures')
    secretaries = relationship('Secretaries', back_populates='procedure', cascade="all, delete-orphan, delete")
    key = relationship('Key', back_populates='procedure', cascade="all, delete-orphan, delete")


class Accreditation(Base):
    __tablename__ = 'accreditation'

    id = Column(String, primary_key=True)
    protocolDate = Column(DateTime)
    protocolNumber = Column(Integer)
    docSerial = Column(String)
    docNumber = Column(String)
    regNumber = Column(String)

    accreditationProcedures = relationship('Procedure', back_populates='accreditation', cascade="all, delete-orphan")

    persons = relationship('Person', back_populates='personAccreditation')
