from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    allow_methods=[""],
    allow_headers=[""],
)

my_jobs =[{"title": "FRONTEND Developer","content": "WebAP","id":1},
{"title":"Python Developer","content":"FASTAPI","id":2}]

job_cat = [{"jobcategory":"Python","id":1},{"jobcategory":"Ruby","id":2}]



def find_job(id):
    for j in my_jobs:
        if j["id"] == id:
            return j
def find_job_category(id):
    for i in job_cat:
        if i["id"] == id:
            return i            



@app.get("/")
async def main():
    return {"message": "Hello World"}



@app.get("/jobs/designe")
def get_job_list():
    return my_jobs



@app.get("/jobs/{id}")
def get_job_with_id(id):
    job = find_job(int(id))
    return job

@app.get('/cat/{id}')
def get_job_cat(id):
    job_cat = find_job_category(int(id))
    return job_cat
    
  