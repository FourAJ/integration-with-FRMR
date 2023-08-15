from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from frmr_api.database.database import Base


class Postgraduate(Base):
    __tablename__ = 'postgraduate'

    postgraduateId = Column(String, primary_key=True)
    isDuplicate = Column(Boolean)
    educPlace = Column(Integer)
    educationStageId = Column(Integer)
    educationStageName = Column(String)
    isStudying = Column(Boolean)
    beginYear = Column(Integer)
    docSerial = Column(String)
    docNumber = Column(String)
    docDate = Column(DateTime)
    institutionId = Column(Integer)
    institutionName = Column(String)
    academicDegreeId = Column(Integer)
    academicDegreeName = Column(String)
    scienceBranchId = Column(Integer)
    scienceBranchName = Column(String)
    specId = Column(Integer)
    specName = Column(String)
    doctSpecId = Column(Integer)
    doctSpecName = Column(String)
    additionSpecId = Column(Integer)
    additionSpecName = Column(String)
    isTargeted = Column(Boolean)
    targetedRegionId = Column(Integer)
    dutyMonthsPeriod = Column(Integer)
    dutyYearsPeriod = Column(Integer)
    isTargetTerminated = Column(Boolean)
    terminationReasonId = Column(Integer)
    dutyInfo = Column(String)
    oksmId = Column(Integer)
    oksmName = Column(String)
    unionRepublicId = Column(Integer)
    unionRepublicName = Column(String)
    foreignInstitution = Column(String)
    hasForeignCert = Column(Integer)
    foreignCertSerial = Column(String)
    foreignCertNumber = Column(String)
    foreignCertDate = Column(DateTime)

    person_oid = Column(String, ForeignKey('person.oid', ondelete='CASCADE'))
    person = relationship('Person', back_populates='personPostgraduate')
