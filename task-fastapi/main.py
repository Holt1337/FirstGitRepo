from pip._vendor.requests import packages
from  pydantic import BaseModel
from typing import Union
from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from enum import Enum

[packages]
fastapi = "*"
uvicorn = "*"

from fastapi import FastAPI, Header

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World!"}

class Timestampp(BaseModel):
    id: Union[int, None]=None
    timestamp: Union[int, None]=None

@app.post('/post')
async def get_post(item: Timestampp):
    item.id = 0
    item.timestamp = 0
    return item


class DogType(str, Enum):
    terrier = 'terrier'
    bulldog = 'bulldog'
    dalmatian = 'dalmatian'

class Dogs(BaseModel):
    name: str
    pk: Union[int, None] = None
    kind: DogType

@app.get('/dog')
async def get_dogs(dog: Dogs):
    #dog.pk = 0
    return dog

@app.post('/dog')
async def create_dog(dog: Dogs):
    dog.pk = 0
    return dog

@app.get('/dog/{pk}')
async def get_dog_by_pk(pk: int, dog: Dogs):
    dog.pk = pk
    return dog

@app.get('/dog/{type}')
async def get_dog_by_type(type: DogType, dog: Dogs):
    dog.kind = type
    return dog

@app.patch('/dog/{pk}')
async def update_dog(pk: int, dog: Dogs):
    dog.pk = pk
    return dog



