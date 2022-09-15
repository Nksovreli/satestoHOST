import models,schemas,utils
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
import database
from database import engine,get_db
from typing import List



router = APIRouter(
    prefix="/users",  
    tags = ['Users']
)


@router.get('/')
def get_users(db: Session = Depends(get_db)):
    posts = db.query(models.User).all()
    return posts



@router.post('/create',status_code=status.HTTP_201_CREATED,
response_model = schemas.UserOut)
def create_user(user:schemas.UserCreate,db: Session = Depends(get_db)):

    hashed_password =utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
