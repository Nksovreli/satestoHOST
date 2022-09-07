from fastapi import FastAPI



app = FastAPI()




@app.get('/')
async def home():
    return {"data":"Hellow"}


@app.get('/jobs')
def jobs():
    return {"msg":"jobs"}