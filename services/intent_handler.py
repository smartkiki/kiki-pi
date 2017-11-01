#intent_handler service
from ..nlp import response as nlp
from . import weather_service as ws
nlp_handler = nlp.Response()

def intent_handler(intent, entities):
	if intent == 'weather':
		#handle weather
		print "Got to weather intent"
		city = entities
		weather = ws.get_city_weather(city)
		return "The temperature in %s is %d degrees Celsius" % (city, int(round(weather - 273.15)))
	else:
		#handle other intents
		print "got to some other intent"
		print intent
		return ""