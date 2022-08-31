import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps

owm = OWM('e72eae55fc7f21e4df8629ab4f89d474')
mgr = owm.weather_manager()
bot = telebot.TeleBot("5648043013:AAGh9wpvDpSfnhIGPrT7Y41d1HxaCF0Bmxk")

config_dict = get_default_config()
config_dict['language'] = 'ru'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Здарова, голова!👹" + "\n" + "Не хочешь узнать погоду в каком нибудь городе/стране? Напиши название...✍🏼")

@bot.message_handler(content_types=['text'])
def send_weather(message):
	observation = mgr.weather_at_place(message.text)
	daily_forecaster = mgr.forecast_at_place(message.text,'3h')

	w = observation.weather
	tomorrow = timestamps.tomorrow()
	weather = daily_forecaster.get_weather_at(tomorrow)

	temp = w.temperature('celsius')["temp"]
	wind = w.wind()["speed"]

	answer = "В городе/стране " + message.text + " сейчас: " + w.detailed_status + "🌍" + "\n"
	answer += "Скорость ветра: "+ str(wind) + "м/с" + "\n"
	answer += "Температура сейчас в районе: " + str(temp) + "°C" + "\n"

	if 0 <= temp <= 20:
		answer += "Пора одевать вещи потеплее! Близится осень...😵‍💫" + "\n\n"
	elif temp < 0:
		answer += "Сегодня дубарь, пора бы серьезно одеться! 🥶" + "\n\n"
	elif temp >= 33:
		answer += "В аду сегодня жарко, запасись водой! 🤬" + "\n\n"
	else:
		answer += "Погода сегодня бомба 🥳" + "\n\n"

	answer += "Завтра будет " + weather.detailed_status + " 👀"

	bot.send_message(message.chat.id, answer)

bot.infinity_polling( none_stop = True)
