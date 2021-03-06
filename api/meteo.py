from typing import Dict, Optional, Union
import fastapi
from fastapi import Depends
from models.location import Location
from models.validation_errors import ValidationError
from services import openweather_service


router = fastapi.APIRouter()

@router.get('/api/meteo/{city}')
async def meteo(loc: Location = Depends(),
          units: Optional[str] = 'metric'
          ):
    try:
        report =  await openweather_service.get_reports(loc.city, loc.state, loc.country, units)
        return report
    except ValidationError as ve:
        return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)
    
