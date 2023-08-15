from typing import List
from pydantic import BaseModel
from pydantic.validators import datetime


class EducationType(BaseModel):
    code: int
    name: str

    class Config:
        orm_mode = True


class Course(BaseModel):
    enrollmentRate: int
    structuralUnitStudent: str
    enrollmentSpecialtyId: int
    learningOutcomeId: int
    protocolNumber: str
    dateIssueProtocol: datetime
    diplomaQualificationId: int
    reasonForExpulsionId: int
    dateDeduction: datetime
    transferDate: datetime
    dateAcademicLeave: datetime
    educationalOrgEndCourseId: int
    academicDegreeId: int
    scientificDegreeId: int

    class Config:
        orm_mode = True


class EducationProf(BaseModel):
    profId: str
    isStudentEducation: bool
    hasForeignProfEducation: bool
    isDuplicate: bool
    educPlace: int
    educationTypeId: EducationType
    beginYear: int
    enrollmentDate: datetime
    courses: List[Course]
    hasDiploma: bool
    docSerial: str
    docNumber: str
    docDate: datetime
    institutionId: int
    institutionName: str
    levelEducation: int
    formEducation: str
    budget: bool
    specId: int
    specName: str
    qualificationId: int
    qualificationName: str
    isTargeted: bool
    targetedRegionId: int
    dutyMonthsPeriod: int
    dutyYearsPeriod: int
    isTargetTerminated: bool
    terminationReasonId: int
    dutyInfo: str
    oksmId: int
    oksmName: str
    unionRepublicId: int
    unionRepublicName: str
    foreignInstitution: str
    hasForeignCert: int
    foreignCertSerial: str
    foreignCertNumber: str
    foreignCertDate: datetime

    class Config:
        orm_mode = True


class EducationProfs(BaseModel):
    educationProf: List[EducationProf]

    class Config:
        orm_mode = True
        from_orm = True
