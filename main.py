from fastapi import FastAPI,response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


@app.get('/')
async def home():
    data = {"id":1}
    return response(content = data)


@app.get('/jobs')
def jobs():
    return {"msg":"jobs"}