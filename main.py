from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def home():
    return {"Hello":"World"}

@app.get('/{name}')
def home(name:str):
    return {"Hello":name}