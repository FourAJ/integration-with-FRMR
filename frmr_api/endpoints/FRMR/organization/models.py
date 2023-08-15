from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from frmr_api.database.database import Base


class Organization(Base):
    __tablename__ = 'organization'

    id = Column(Integer, primary_key=True, autoincrement=True)
    organizationId = Column(String)
    beginDate = Column(DateTime)
    endDate = Column(DateTime)
    entityId = Column(String)

    person_oid = Column(String, ForeignKey('person.oid', ondelete='CASCADE'))
    person = relationship('Person', back_populates='personOrganization')
