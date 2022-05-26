from fastapi import FastAPI
import uvicorn
from starlette.staticfiles import StaticFiles

from api import meteo
from views import home

app = FastAPI()

def configure():
    configure_routers()

def configure_routers():
    app.mount('/static', StaticFiles(directory = 'static'), name = 'static')
    app.include_router(meteo.router)
    app.include_router(home.router)

if __name__ == '__main__':
    uvicorn.run(app, port='8080', host='127.0.0.1')
    configure()
else:
    configure()