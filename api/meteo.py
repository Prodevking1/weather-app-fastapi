import fastapi

router = fastapi.APIRouter()

@router.get('/api/meteo/{city}')
def meteo(city:str):
    return "Quelques previsions pour" + city
