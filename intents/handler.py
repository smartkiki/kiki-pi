import weather
import alarm
import take_image
import object_recognition
import default
import greetings
import music
import search
import calendar

INTENT_MAP = {
	'greetings' : greetings,
    'get-weather' : weather,
    'alarms': alarm,
    'take_image': take_image,
    'object_recognition': object_recognition,
    'music' : music,
    'web_search' : search,
    'calendar' : calendar,
    #'uber' : uber,
}


def handle_intent(intent, entities):
    handler = INTENT_MAP.get(intent, default)
    return handler.execute_intent(entities)
