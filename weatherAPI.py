import requests
import json
from pprint import pprint

url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}"
# xxxxxには取得したAPIキーを入れる
url = url.format(city_name = "Tokyo", API_key = "xxxxx")

jsondata = requests.get(url).json()
pprint(jsondata)

{'base': 'stations',
 'clouds': {'all': 75},
 'cod': 200,
 'coord': {'lat': 35.6895, 'lon': 139.6917},
 'dt': 1687917481,
 'id': 1850144,
 'main': {'feels_like': 35.33,
          'humidity': 66,
          'pressure': 1010,
          'temp': 30.54,
          'temp_max': 32.55,
          'temp_min': 27.75},
 'name': 'Tokyo',
 'sys': {'country': 'JP',
         'id': 2001249,
         'sunrise': 1687894045,
         'sunset': 1687946462,
         'type': 2},
 'timezone': 32400,
 'visibility': 8000,
 'weather': [{'description': 'broken clouds',
              'icon': '04d',
              'id': 803,
              'main': 'Clouds'}],
 'wind': {'deg': 180, 'speed': 5.14}}

print("天気：",jsondata["weather"][0]["main"])
print("天気詳細：",jsondata["weather"][0]["description"])

print("都市名：",jsondata["name"])
print("気温：",jsondata["main"]["temp"])
print("体感気温：",jsondata["main"]["feels_like"])
print("最低気温：",jsondata["main"]["temp_min"])
print("最高気温：",jsondata["main"]["temp_max"])
print("気圧：",jsondata["main"]["pressure"])
print("湿度：",jsondata["main"]["humidity"])

print("風速：",jsondata["wind"]["speed"])
print("風の方角：",jsondata["wind"]["deg"])
