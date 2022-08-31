from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps
from pyowm.utils import config
from colorama import Fore, Back, Style
from colorama import init

init()

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('e72eae55fc7f21e4df8629ab4f89d474')
mgr = owm.weather_manager()

place = input("В каком городе/стране вас интересует погода?: ")

observation = mgr.weather_at_place(place)
daily_forecaster = mgr.forecast_at_place(place, '3h')
w = observation.weather

tomorrow = timestamps.tomorrow()                                   
weather = daily_forecaster.get_weather_at(tomorrow) 

temp = w.temperature('celsius')["temp"]
wind = w.wind()["speed"] 

print("В городе " + place + " сейчас: " + w.detailed_status)
print("Скорость ветра: "+ str(wind) + "м/с")
print("Температура сейчас в районе: " + str(temp) + "°C")
print("Завтра будет " + weather.detailed_status + "!")

if 10 <= temp <= 20:
	print(Fore.BLACK); print(Back.YELLOW);
	print("Одевайся теплее! Близится осень...")
elif temp < 10:
	print(Fore.BLACK); print(Back.CYAN);
	print("Сегодня дубарь, пора бы одеться! ")
elif temp >= 33:
	print(Fore.BLACK); print(Back.RED);
	print("В аду сегодня жарко, запасись водой!")
else:
	print(Fore.BLACK); print(Back.GREEN);
	print("Погода бомба :D")
input()