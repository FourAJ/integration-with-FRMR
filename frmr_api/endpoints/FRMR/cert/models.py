from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from frmr_api.database.database import Base


class EducationCert(Base):
    __tablename__ = 'cert'

    certId = Column(String, primary_key=True)
    institutionId = Column(Integer)
    institutionName = Column(String)
    certSerial = Column(String)
    certNumber = Column(String)
    examDate = Column(DateTime)
    passDate = Column(DateTime)
    endDate = Column(DateTime)
    specId = Column(Integer)
    specName = Column(String)

    person_oid = Column(String, ForeignKey('person.oid', ondelete='CASCADE'))
    person = relationship('Person', back_populates='educationCert')
