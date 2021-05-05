import requests

class WeatherService:

    baseUrl = "https://api.openweathermap.org/data/2.5/forecast"
    appId = "get your own from the website"

    @classmethod
    def getForecast(cls, city, country):
        resp = requests.get(cls.baseUrl, {"q": f"{city},{country}", "mode": "json", "APPID": cls.appId})
        return resp.json()["list"]

if __name__ == "__main__":
    print(WeatherService.getForecast("London", "England"))

