from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,Response,status,HTTPException,Depends,Request
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional,List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from database import engine,get_db
import models,schemas
import routers
from routers import users, jobs



models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://localhost/https:/fastapi-ipove.herokuapp.com/",
    "https://localhost.fastapi-ipove.herokuapp.com/",
    "http://localhost/",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# def find_job(id):
#     for j in my_jobs:
#         if j["id"] == id:
#             return j
# def find_job_category(id):
#     for i in job_cat:
#         if i["id"] == id:
#             return i            



# @app.get("/")
# async def main():
#     return {"message": "Hello World"}



# @app.get("/jobs/designe")
# def get_job_list():
#     return my_jobs



# @app.get("/jobs/{id}")
# def get_job_with_id(id):
#     job = find_job(int(id))
#     return job

# @app.get('/cat/{id}')
# def get_job_cat(id):
#     job_cat = find_job_category(int(id))
#     return job_cat

# @app.get('/cat') 
# def show_all_cars():
#     return card_list  

# @app.get('/vr')
# def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return posts

# @app.post('/addjob',status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
# def add_job(job:schemas.JobCreate,db: Session = Depends(get_db)):
#     new_job = models.Post(**job.dict())
#     db.add(new_job)
#     db.commit()
#     db.refresh(new_job)

#     return new_job

# @app.get("/vr/{id}")
# def get_id(id,db: Session = Depends(get_db)):
#     job = post = db.query(models.Post).filter(models.Post.id==id).first()
#     if not job:
#         if not post:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
#     return job




#app.include_router(jobs.router)

app.include_router(jobs.router)
app.include_router(users.router)