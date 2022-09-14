from pydantic import BaseModel,EmailStr
from datetime import datetime

class JobCreate(BaseModel):
    id:int
    title:str
    content:str 
    salary:int
    emprequest:str
    


class Post(BaseModel):
    id:int
    title:str
    content:str 
    salary:int
    emprequest:str



    class Config:
        orm_mode = True


class UpdateJob(BaseModel):
    pass