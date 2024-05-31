import time
from datetime import timedelta

from weather_service import WeatherService, WeatherServiceProxy

if __name__ == "__main__":
    weather_service = WeatherService()
    proxy = WeatherServiceProxy(weather_service, cache_duration=timedelta(seconds=5))

    print(proxy.get_weather("New York"))
    time.sleep(2)
    print(proxy.get_weather("New York"))

    # Wait for cache to expire
    time.sleep(6)
    print(proxy.get_weather("New York"))
