from pydantic import BaseModel,EmailStr
from datetime import datetime

class JobCreate(BaseModel):
    title:str
    content:str 
    


class Post(BaseModel):
    id:int
    title:str
    content:str
    published:bool
    created_at:datetime 

    class Config:
        orm_mode = True