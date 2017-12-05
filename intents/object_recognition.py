import requests

from ..camera.image_capture import capture


OBJECT_RECOGNITION_URL = 'http://localhost/object_recognition'
CHATBOT_URL = 'http://localhost:8082/uploadimage'


def execute_intent(entities):
    image_name = capture()
    files = {'file': open(image_name)}
    response = requests.post(OBJECT_RECOGNITION_URL, files=files)
    return 'Object in front of camera is ' + response.text
