import models,schemas,auth2
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
import database
from database import engine,get_db
from typing import List,Optional

router = APIRouter(
    prefix="/jobs",  
    tags = ['Jobs']
)

k= []
@router.get('/search')
def search(query: Optional[str] = None,db: Session = Depends(get_db)):
    job = db.query(models.Post).filter(models.Post.title.contains(query)).all()
    
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return job   

   
   
   
   


@router.get('/')
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@router.post('/add',status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def add_job(job:schemas.JobCreate,db: Session = Depends(get_db),
current_user: int = Depends(auth2.get_current_user)):
    new_job = models.Post(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job


@router.get("/{id}")
def get_id(id,db: Session = Depends(get_db)):
    job = db.query(models.Post).filter(models.Post.id==id).first()
    if not job:
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return job    



@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db),
current_user: int = Depends(auth2.get_current_user)):
    job = db.query(models.Post).filter(models.Post.id==id)
   
    if job.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} does not exist')
    job.delete(synchronize_session=False) 
    db.commit()


@router.put('/{id}')
def update_job(id: int,updated_job: schemas.UpdateJob,db: Session = Depends(get_db),
current_user: int = Depends(auth2.get_current_user)):

    job_query= db.query(models.Post).filter(models.Post.id == id)
    job = job_query.first()
    print(updated_job)

    if job == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} does not exist')
    job_query.update(updated_job.dict(),synchronize_session=False)  
    print(updated_job.dict())      
    db.commit()                


   
    return job_query.first()

   



@router.get("/person/{id}")
def get_id(id:int,db: Session = Depends(get_db)):
    job = db.query(models.Post).filter(models.Post.owner_id == id).all()
    if not job:
        if not job:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return job    



# @router.get('/search')
# def search_job(text:Optional[str],db: Session = Depends(get_db)):
#     jobsearch = db.query(models.Post).filter(Post.title.contains(text)).all()
#     return {"jobs":jobsearch}


   
