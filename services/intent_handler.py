#intent_handler service
import datetime
from multiprocessing import Process
from nlp import response as nlp
from . import weather_service as ws
from . import alarm_service as als
from camera.image_capture import capture


OBJECT_RECOGNITION_URL = 'http://localhost/object_recognition'
nlp_handler = nlp.Response()


def intent_handler(intent, entities):
    if intent == 'weather':
        #handle weather
        print "Got to weather intent"
        #print entities

        city = entities['location']['city']
        weather = ws.get_city_weather(city)
        return "The temperature in %s is %d degrees Celsius" % (city, int(round(weather - 273.15)))
    elif intent == 'alarm':
        #alarm handling here
        print entities
        time = entities['time']
        alarm_time = datetime.datetime.strptime(time, '%H:%M:%S').time()
        p = Process(target=als.alarm_process, args=(alarm_time,))
        p.start()
        return "Set an alarm for %s" % alarm_time.strftime("%I:%M %p")
    elif intent == 'take_image':
        image_name = capture()
        return 'I took the image for you'
    elif intent == 'object_recognition':
        image_name = capture()
        files = {'file': open(image_name)}
        response = requests.post(OBJECT_RECOGNITION_URL, files=files)
        return 'Object in front of camera is ' + response.text
    else:
        #handle other intents
        print("got to some other intent")
        print(intent)
        return ""
