from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from frmr_api.database.database import Base


class EducationCommon(Base):
    __tablename__ = 'common'

    commonId = Column(String, primary_key=True)
    institution = Column(String)
    docSerial = Column(String)
    docNumber = Column(String)
    docDate = Column(DateTime)

    persons = relationship('Person', back_populates='educationCommon')
    profCourseSet = relationship('ProfCourseSet', back_populates='common', cascade="all, delete-orphan")


class ProfCourseSet(Base):
    __tablename__ = 'profcourse'

    id = Column(Integer, primary_key=True, autoincrement=True)

    docDate = Column(DateTime)
    profCourseId = Column(Integer)
    profCourseName = Column(String)

    commonId = Column(String, ForeignKey('common.commonId', ondelete='CASCADE'))
    common = relationship('EducationCommon', back_populates='profCourseSet')
