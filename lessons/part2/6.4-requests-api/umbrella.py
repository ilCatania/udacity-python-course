import sys
import time
import datetime
from weatherService import WeatherService

def within_time(item, start, end):
    dt = datetime.datetime.fromtimestamp(item["dt"])
    return dt > start and dt < end

def makeUmbrellaDecision(city: str, country: str) -> bool:
    current_time = datetime.datetime.now()
    end_time = current_time + datetime.timedelta(hours=12)
    forecast = WeatherService.getForecast(city, country)
    applicable_forecast = (f for f in forecast if within_time(f, current_time, end_time))
    rain_probabilities = [f["rain"]["3h"] for f in applicable_forecast if "rain" in f]
    return len(rain_probabilities) and max(rain_probabilities) > 0.1
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Need to specify city and country!")
    else:
        city = sys.argv[1]
        country = sys.argv[2]
        s = "" if makeUmbrellaDecision(city, country) else " not"
        print(f"You will{s} need an umbrella in {city}, {country} today.")

