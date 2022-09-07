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


@app.get("/")
async def main():
    return {"message": "Hello World"}