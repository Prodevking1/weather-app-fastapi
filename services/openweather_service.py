from typing import Optional
import requests


async def get_reports (city:str, state:Optional[str], country:str, units:str):
    q = f"{city},{country}"
    key = '91f20fef6924822ab6748495265321b5'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={key}'
    print(url)
    response = requests.get(url)
    return response.json()
