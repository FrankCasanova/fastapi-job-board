from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# shared properties
class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


# this will be used to velidate the data while creating a Job


class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str


# this will be used to format the repsponse to not have id, owned_id, etc...
class ShowJob(JobBase):
    title: str
    company: str
    location: str
    description: str
    date_posted: date
    company_url: Optional[str]

    class Config:  # to convert non dict obj to json
        orm_mode = True
