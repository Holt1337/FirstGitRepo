from pip._vendor.requests import packages
from  pydantic import BaseModel
from typing import Union, List
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
    #item.id = 0
    #item.timestamp = 0
    return item


class DogType(str, Enum):
    terrier = 'terrier'
    bulldog = 'bulldog'
    dalmatian = 'dalmatian'

class Dogs(BaseModel):
    name: str
    pk: Union[int, None] = None
    kind: DogType

dogs_list = []


@app.get('/dog')
async def get_dogs(kind: DogType = None):
    list = []
    for dog in dogs_list:
        if dog.kind == kind:
            list.append(dog)

    #dog.kind = kind
    return list

@app.post('/dog', response_model=Dogs)
async def create_dog(dog: Dogs):
    if dog.pk:
        1 == 1
    else:
        dog.pk = len(dogs_list)
    dogs_list.append(dog)
    return dog

@app.get('/dog/{pk}', response_model=Dogs)
async def get_dog_by_pk(pk: int):
    for dog in dogs_list:
        if dog.pk == pk:
            return dog

    raise HTTPException(404)

@app.get('/dog/{type}', response_model=Dogs)
async def get_dog_by_type(type: DogType):
    for dog in dogs_list:
        if dog.kind == type:
            return dog

    raise HTTPException(404)

@app.patch('/dog/{pk}', response_model=Dogs)
async def update_dog(pk: int, ndog: Dogs):
    for dog in dogs_list:
        if dog.pk == pk:
            dog.kind = ndog.kind
            dog.name = ndog.name
            dog.pk = ndog.pk

            return dog

    raise HTTPException(404)

