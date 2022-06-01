from typing import Dict, Optional, Union
from anyio import Any
import fastapi
from fastapi import Depends
from models.location import Location
from services import openweather_service


router = fastapi.APIRouter()

@router.get('/api/meteo/{city}')
async def meteo(loc: Location = Depends(),
          units: Optional[str] = 'metric'
          ):
    report =  await openweather_service.get_reports(loc.city, loc.state, loc.country, units)
    return report
