from typing import List

from db.repository.jobs import create_new_job
from db.repository.jobs import list_jobs
from db.repository.jobs import retrieve_job
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.jobs import JobCreate
from schemas.jobs import ShowJob
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/create-job/", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    """
    Create a new job
    """
    current_user = 1
    job = create_new_job(job=job, db=db, owner_id=current_user)
    return job


# if we keep just '{id}' it wuld start catching all routes
@router.get("/get/{id}", response_model=ShowJob)
def read_job(id: int, db: Session = Depends(get_db)):
    """
    Get a job by id
    """
    job = retrieve_job(id=id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id: {id} does not exist.",
        )
    return job


@router.get("/all", response_model=List[ShowJob])
def read_jobs(db: Session = Depends(get_db)):
    """
    Get all jobs
    """
    jobs = list_jobs(db=db)
    return jobs
