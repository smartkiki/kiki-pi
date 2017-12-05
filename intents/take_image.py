from ..camera.image_capture import capture
import requests

CHATBOT_URL = 'http://localhost:8082/uploadimage'

def execute_intent(entities):
    #image_name = capture()
    #files = {'file': open(image_name)}
    print "Got to image capture intent"
    data = _create_json_for_request()
    response = requests.post(CHATBOT_URL, json=data)
    print "got to after response"
    return 'Done! The image has successfully been sent to your mobile device'

def _create_json_for_request():
	data = { 
		"fbid" : "1725030900888096",
		"url" : "https://www.w3schools.com/css/trolltunga.jpg"
	}
	return data