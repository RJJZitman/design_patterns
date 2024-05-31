import time
from datetime import datetime, timedelta


class WeatherData:
    def __init__(self, temperature: float, humidity: float, condition: str):
        self.temperature = temperature
        self.humidity = humidity
        self.condition = condition

    def __str__(self):
        return f"Temperature: {self.temperature}°C, Humidity: {self.humidity}%, Condition: {self.condition}"


class WeatherService:
    def get_weather(self, location: str) -> WeatherData:
        print(f"Fetching weather data for {location} from external API...")
        # Simulating an expensive API call
        time.sleep(2)
        # Returning mock data
        return WeatherData(25.0, 60, "Sunny")


class CacheEntry:
    def __init__(self, data: WeatherData, timestamp: datetime):
        self.data = data
        self.timestamp = timestamp


class WeatherServiceProxy:
    def __init__(self, service: WeatherService, cache_duration: timedelta):
        self.service = service
        self.cache_duration = cache_duration
        self.cache: dict[str, CacheEntry] = {}

    def get_weather(self, location: str) -> WeatherData:
        current_time = datetime.now()
        if location in self.cache:
            entry = self.cache[location]
            if current_time - entry.timestamp < self.cache_duration:
                print(f"Returning cached weather data for {location}")
                return entry.data
            else:
                print(f"Cache expired for {location}")
        else:
            print(f"No cache found for {location}")

        weather_data = self.service.get_weather(location)
        self.cache[location] = CacheEntry(weather_data, current_time)
        return weather_data
