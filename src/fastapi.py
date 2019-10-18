from fastapi import FastAPI

# https://github.com/tiangolo/fastapi
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# import requests
# result = requests.get('http://127.0.0.1:8000')
# result.json()
