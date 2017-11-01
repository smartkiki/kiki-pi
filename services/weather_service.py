import requests

WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q="
WEATHER_APP_ID = '&appid=51bb2b6738febb93036279f23fcd067c'


def get_city_weather(cityname):
	print "got to this function with city %s" % cityname
	URL = WEATHER_BASE_URL + cityname + WEATHER_APP_ID
	print "created url: %s" % URL
	r = requests.get(url = URL)
	data = r.json()
	print data['main']['temp']
	return data['main']['temp']