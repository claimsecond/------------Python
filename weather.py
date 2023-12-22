from coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather

async def main():
    coordinates = await get_gps_coordinates()
    weather = await get_weather(coordinates=coordinates)
    print(format_weather(weather))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
