import fastapi
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

templates = Jinja2Templates(directory ='templates')
router = fastapi.APIRouter()

@router.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@router.get('/favicon.ico')
def favicon():
    return fastapi.response.RedirectResponse(url = '/favicon.ico')