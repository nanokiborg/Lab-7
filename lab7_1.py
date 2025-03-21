import requests
import json 


WEATHER_API_KEY = "fb50eed1b9efe0e2f8660950a8e70f51"


def weather_loc(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}"

    response = requests.get(url)
    data = response.json()

    return data["weather"][0]["description"], data["main"]["pressure"], data["main"]["humidity"]


if __name__ == '__main__':
    city_name = input('Введите название города:')
    weather, pressure, humidity = weather_loc(city_name)

    print(f' Погода в {city_name}: \n Погода - {weather} \n Атмосферное давление - {pressure} Гектопаскаль  \n Влажность - {humidity}%')