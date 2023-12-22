from weather_api_service import Weather

def format_weather(weather: Weather) -> str:
    """Returns formatted weather data"""
    return (f"{weather.city}, температура {weather.temperature}°C, "
            f"{weather.weather_type}\n")
            # f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
            # f"Закат: {weather.sunset.strftime('%H:%M')}\n")

if __name__ == "__main__":
    from datetime import datetime
    from weather_api_service import WeatherType
    print(format_weather(Weather(
        temperature=25,
        weather_type=WeatherType.Sunny,
        city="Moscow"
    )))