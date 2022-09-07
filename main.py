from fastapi import FastAPI,response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()




@app.get('/')
async def home():
    return {"data":"Hellow"}


@app.get('/jobs')
def jobs():
    return {"msg":"jobs"}