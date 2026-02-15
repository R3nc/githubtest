from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.post("/")
def create():
    return{"hello": "world"}