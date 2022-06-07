from functools import cache
from typing import Optional
from fastapi import Response
import httpx
from api.infrastructures.cache import set_weather

from models.validation_errors import ValidationError


async def get_reports (city:str, state:Optional[str], country:str, units:str):
    q = f"{city},{country}"
    key = '91f20fef6924822ab6748495265321b5'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={key}&units={units}'
    print(url)
    async with httpx.AsyncClient() as client:
        resp : Response = await client.get(url, timeout=60)
        if resp.status_code != 200:
            raise ValidationError(resp.text, resp.status_code)
        
    data = resp.json()
    weather = data['weather']
    main = data['main']
    wind = data['wind']
    sys = data['sys']
    forecast = {'weather': weather,
                'main': main,
                'wind': wind,
                'sys': sys}
    
    return forecast