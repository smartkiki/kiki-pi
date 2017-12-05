import requests


WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q="
WEATHER_APP_ID = '&appid=51bb2b6738febb93036279f23fcd067c'
DEFAULT_LOCATION = 'West Lafayette'


def execute_intent(entities):
    print("Got to weather intent")
    flag = 0
    for e in entities:
        if e.name == 'location':
            print "location we found was {}".format(e.raw)
            LOCATION = e.raw
            flag = 1
            break
    if not flag:
        LOCATION = DEFAULT_LOCATION
    weather = _get_city_weather(LOCATION)
    
    return _get_formatted_weather(LOCATION, weather)


def _get_city_weather(cityname):
    print("got to this function with city %s" % cityname)
    URL = WEATHER_BASE_URL + cityname + WEATHER_APP_ID
    print("created url: %s" % URL)
    r = requests.get(url=URL)
    data = r.json()
    print(data['main']['temp'])
    return data['main']['temp']

def _get_formatted_weather(city, weather):
    temperature = int(weather) - 273.15
    return "The temperature in %s is %d degrees Celsius." % (city, temperature)