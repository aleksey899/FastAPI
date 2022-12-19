from fastapi import FastAPI
import uvicorn
import os

second_app = FastAPI()

@second_app.get('/')
def root():
    return {'datakey':'necontent'}


@second_app.get("/get_data")
def get_data():
    return {'datakey':'hello world'}

if __name__ == '__main__':
    uvicorn.run('second_app:second_app',host='0.0.0.0',port=80,reload=True)