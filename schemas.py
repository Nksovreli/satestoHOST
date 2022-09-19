from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class JobCreate(BaseModel):
    title:str
    content:str 
    salary:int
    emprequest:str
    owner_id:int
    username:str
    category_id:int 


    



class Post(BaseModel):
    id:int
    title:str
    content:str 
    salary:int
    emprequest:str
    created_at:datetime
    username:str
    category_id:int

    






    class Config:
        orm_mode = True


class UpdateJob(BaseModel):
    title:str
    content:str
    salary:int
    emprequest:str


class UserCreate(BaseModel):
    email:EmailStr
    password:str
    name:str  
    last_name:str
    number:str


class Token(BaseModel):
    access_token:str 
    token_type:str  


class TokenData(BaseModel): 
    id:Optional[str] = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at:datetime 
    name:str  
    last_name:str
    number:str

    class Config:
        orm_mode = True   


class JobResponse(BaseModel):
    id:int
    title:str
    content:str 
    salary:int
    emprequest:str
    created_at:datetime
    owner_id:int
    username:str
    
    class Config:
        orm_mode = True


# class JobSearch(BaseModel):
#     title:str
#     content:str
#     salary:int
#     emprequest:str
#     created_at:datetime

#     class Config:
#         orm_mode = True
