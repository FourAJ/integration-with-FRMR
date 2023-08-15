from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from frmr_api.database.database import Base


class Qualification(Base):
    __tablename__ = 'qualification'

    qualificationId = Column(String, primary_key=True)
    qualifyCategoryId = Column(Integer)
    qualifyCategoryName = Column(String)
    beginDate = Column(DateTime)
    endDate = Column(DateTime)
    specId = Column(Integer)
    specName = Column(String)
    fedPostId = Column(Integer)
    fedPostName = Column(String)
    postId = Column(Integer)
    postName = Column(String)

    person_oid = Column(String, ForeignKey('person.oid', ondelete='CASCADE'))
    person = relationship('Person', back_populates='personQualification')
