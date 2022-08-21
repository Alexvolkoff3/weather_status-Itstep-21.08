"""
Есть 2 версии задания. Можете выполнить оба, либо одно из них.
1. Получить данные о погоде по апи.
Сайт и документация: https://www.metaweather.com/api/

 - Сделать запрос по адресу https://www.metaweather.com/api/location/search/?query=kiev
 - Из ответа достать id погодной зоны, по ключу woeid
 - Сделать запрос по адресу https://www.metaweather.com/api/location/{woeid}/
 - Из ответа получить следующие данные: температура, влажность, скорость ветра.
 """

# 21/08 т.к Мета не работает, сделал дз с помощью openweathermap, Api_key

import requests


api_key = "44f0ade2088cce94e717516be445967f"  # для задания выложил публично
url = 'https://api.openweathermap.org/data/2.5/weather'

weather_params = {
    'lat': 50.4333,  # достал координаты когда использовал Апишку с параметром города "q" там выдает автоматом координаты
    'lon': 30.5167,  # не прописывал код т.к. был бы дубляж кода
    'appid': api_key,
    'units': 'metric',
    'lang': 'ua',
    'wind': 'wind.speed.unit',

}

response = requests.get(url, params=weather_params)
response.raise_for_status()
weather = response.json()
weather_general_info = response.json()['weather'][0]['description']
weather_temp = response.json()['main']['temp']
weather_humidity = response.json()['main']['humidity']
weather_wind_speed = response.json()['wind']['speed']

print(f"Загальна інформація про погоду: {weather_general_info},\n"
      f"Температура: {weather_temp} градусів за цельсієм,\n"
      f"Вологість: {weather_humidity} %,\n"
      f"Швидкість вітру: {weather_wind_speed} м/c\n")

