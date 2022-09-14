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


@router.get("/{id}")
def get_id(id,db: Session = Depends(get_db)):
    job = post = db.query(models.Post).filter(models.Post.id==id).first()
    if not job:
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return job    



@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db)):
    job = db.query(models.Post).filter(models.Post.id==id)
   
    if job.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} does not exist')
    job.delete(synchronize_session=False) 
    db.commit()


@router.put('/{id}')
def update_post(id: int,updated_job: schemas.UpdateJob,db: Session = Depends(get_db)):

    post_query= db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    db.commit()

    