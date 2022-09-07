from fastapi import FastAPI 

app = FastAPI()


@app.get('/')
async def home():
    return {"MSG":[{"id":1}]}


@app.get('/jobs')
def jobs():
    return {"msg":"jobs"}