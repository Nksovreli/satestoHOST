from fastapi import FastAPI 

app = FastAPI()


@app.get('/')
def home():
    return {"MSG":"Home Page"}


@app.get('/jobs')
def jobs():
    return {"msg":"jobs"}