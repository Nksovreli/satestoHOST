import models,schemas
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
import database
from database import engine,get_db
from typing import List

router = APIRouter(
    prefix="/jobs",  
    tags = ['Jobs']
)



@router.get('/')
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@router.post('/add',status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def add_job(job:schemas.JobCreate,db: Session = Depends(get_db)):
    new_job = models.Post(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job