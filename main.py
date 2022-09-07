from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://fastapi-ipove.herokuapp.com/",
    "https://fastapi-ipove.herokuapp.com/",
    "https://fastapi-ipove.herokuapp.com/",
    "https://fastapi-ipove.herokuapp.com/",
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