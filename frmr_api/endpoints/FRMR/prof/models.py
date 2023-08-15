from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship
from frmr_api.database.database import Base


class EducationType(Base):
    __tablename__ = 'education'

    code = Column(Integer, primary_key=True)
    name = Column(String)

    educationProf = relationship('EducationProf', back_populates='educationTypeId')


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    enrollmentRate = Column(Integer)
    structuralUnitStudent = Column(String)
    enrollmentSpecialtyId = Column(Integer)
    learningOutcomeId = Column(Integer)
    protocolNumber = Column(String)
    dateIssueProtocol = Column(DateTime)
    diplomaQualificationId = Column(Integer)
    reasonForExpulsionId = Column(Integer)
    dateDeduction = Column(DateTime)
    transferDate = Column(DateTime)
    dateAcademicLeave = Column(DateTime)
    educationalOrgEndCourseId = Column(Integer)
    academicDegreeId = Column(Integer)
    scientificDegreeId = Column(Integer)

    educationProf_id = Column(String, ForeignKey('educationProf.profId', ondelete='CASCADE'))
    educationProf = relationship('EducationProf', back_populates='courses')


class EducationProf(Base):
    __tablename__ = 'educationProf'

    profId = Column(String, primary_key=True)
    isStudentEducation = Column(Boolean)
    hasForeignProfEducation = Column(Boolean)
    isDuplicate = Column(Boolean)
    educPlace = Column(Integer)

    educationType = Column(Integer, ForeignKey('education.code'))
    educationTypeId = relationship('EducationType', back_populates='educationProf', lazy='joined')

    beginYear = Column(Integer)
    enrollmentDate = Column(DateTime)

    courses = relationship('Course', back_populates='educationProf', cascade="all, delete-orphan")

    hasDiploma = Column(Boolean)
    docSerial = Column(String)
    docNumber = Column(String)
    docDate = Column(DateTime)
    institutionId = Column(Integer)
    institutionName = Column(String)
    levelEducation = Column(Integer)
    formEducation = Column(String)
    budget = Column(Boolean)
    specId = Column(Integer)
    specName = Column(String)
    qualificationId = Column(Integer)
    qualificationName = Column(String)
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
    person = relationship('Person', back_populates='educationProf')
