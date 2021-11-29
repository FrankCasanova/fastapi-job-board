from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from db.base_class import Base


class Job(Base):

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)
    company_url = Column(String(100))
    location = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=False)
    date_posted = Column(Date, nullable=False)
    owner_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    owner = relationship("User", back_populates="job")
