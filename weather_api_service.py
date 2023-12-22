from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import TypeAlias
import asyncio

# import requests
import aiohttp

import coordinates
from coordinates import Coordinates
import config

Celsius: TypeAlias = int

class WeatherType(str, Enum):
    Sunny = "Ясно" 
    Clear = "Ясно" 
    
    # TODO дописать статусы https://www.weatherapi.com/docs/weather_conditions.json и сделать их отображаемыми

@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: WeatherType
    city: str
    
async def get_weather(coordinates: Coordinates) -> Weather:
    """Returns weather for given coordinates"""
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{config.URL}?key={config.API_KEY}&q={coordinates.latitude},{coordinates.longitude}"
        ) as response:
            weather_data = await response.json()

    weather = _parse_weather(weather_data)

    return weather


def _parse_weather(weatherAPI_response: dict) -> Weather:
    """Parses weatherAPI_response"""
    return Weather(
        temperature=weatherAPI_response["current"]["temp_c"],
        weather_type=weatherAPI_response["current"]["condition"]["text"],
        city=weatherAPI_response["location"]["name"]
    )


if __name__ == "__main__":
    async def main():
        print(await get_weather(coordinates = await coordinates.get_gps_coordinates()))
    
    asyncio.run(main())

