from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class JobCreate(BaseModel):
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


class UpdateJob(JobCreate):
    pass

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    id:int
    access_token:str 
    token_type:str  

    class Config:
        orm_mode = True

class TokenData(BaseModel): 
    id:Optional[str] = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at:datetime 

    class Config:
        orm_mode = True   