#intent_handler service
import datetime
from multiprocessing import Process
from ..nlp import response as nlp
from . import weather_service as ws
from . import alarm_service as als
nlp_handler = nlp.Response()

def intent_handler(intent, entities):
	if intent == 'weather':
		#handle weather
		print "Got to weather intent"
		city = entities
		weather = ws.get_city_weather(city)
		return "The temperature in %s is %d degrees Celsius" % (city, int(round(weather - 273.15)))
	elif intent == 'alarm':
		#alarm handling here
		entities = "21:44:00"
		alarm_time = datetime.datetime.strptime(entities, '%H:%M:%S').time()
		p = Process(target=als.alarm_process, args=(alarm_time,))
		p.start()
		return "Set an alarm for %s" % alarm_time.strftime("%I:%M %p")
	else:
		#handle other intents
		print "got to some other intent"
		print intent
		return ""