from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_off: bool = None

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get('/')
def read_root():
    return {'hello':'world'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = None):
    return {'item_id':item_id,'q':q}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}

@app.get('/users/me')
def reader_user_me():
    return {'user_id':'the current user'}

@app.get('/users/{user_id}')
def reader_user(user_id: str):
    return {'user_id': user_id}

# 自定义类型
@app.get("/model/{model_name}")
def get_model(model_name:ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


# 匹配任何path
@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {'file_path': file_path}

#  "query" parameters

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get('/items')
def read_item(skip: int=0, limit: int=0):
    return fake_items_db[skip : skip + limit]

# @app.get('/items/{item_id}')
# def read_item(item_id: str, q:str = None, short: bool = False):
#     item = {'item_id': item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# @app.get("/items/{item_id}")
# def read_item(item_id: str, q: str = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item