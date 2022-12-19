from fastapi import FastAPI
import requests
import os
import uvicorn

main_app = FastAPI()

@main_app.get("/")
def get_data():
    return {'type':'content'}
    # url =  f'http://{config.host}:{config.port}'
    # result = requests.get(url)
    # if result.status_code == 200:
    #     return result.json()
    # else:
    #     return {'error':'xxxx'} ###

@main_app.get("/get_data")
def get_data():
    url = f'{os.getenv(key="URL")}/get_data'
    try:
        result = requests.get(url)
        if result.status_code == 200:
            return result.json()
        else:
            return {'error':'xxxx'}
    except Exception as ex:
        result = {'error':ex, 'url':url,'url2':os.getenv(key="URL")}
        return result

if __name__ == '__main__':
   uvicorn.run('main_app:main_app',host='0.0.0.0',port=80,reload=True)