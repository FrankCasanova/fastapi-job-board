from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate, ShowJob
from db.repository.jobs import create_new_job, retrieve_job


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
@router.get('/get/{id}', response_model=ShowJob)
def read_job(id: int, db: Session = Depends(get_db)):
    """
    Get a job by id
    """
    job = retrieve_job(id=id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id: {id} does not exist.")
    return job
