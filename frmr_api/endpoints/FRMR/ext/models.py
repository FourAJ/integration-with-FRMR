from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from frmr_api.database.database import Base


class Ext(Base):
    __tablename__ = 'ext'

    extId = Column(String, primary_key=True)
    profEducationKindId = Column(Integer)
    profEducationKindName = Column(String)
    institutionId = Column(Integer)
    institutionName = Column(String)
    hoursCount = Column(Integer)
    theme = Column(String)
    docSerial = Column(String)
    docNumber = Column(String)
    docDate = Column(DateTime)
    specId = Column(Integer)
    specName = Column(String)

    person_oid = Column(String, ForeignKey('person.oid', ondelete='CASCADE'))
    person = relationship('Person', back_populates='personExt')
