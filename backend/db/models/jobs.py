from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean


class Job(Base):

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)
    company_url = Column(String(100))
    location = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=False)
    date_posted = Column(Date, nullable=False)
    is_active = Column(Boolean(), default=True)
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    owner = relationship("User", back_populates="job")
