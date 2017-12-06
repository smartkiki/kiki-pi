import requests

from ..camera.image_capture import capture


OBJECT_RECOGNITION_URL = 'http://web.kiki.28479259.svc.dockerapp.io/object_recognition'


def execute_intent(entities):
    image_name = capture()
    files = {'file': open(image_name)}
    response = requests.post(OBJECT_RECOGNITION_URL, files=files)
    return 'Object in front of camera is ' + response.text
