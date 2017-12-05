from ..camera.image_capture import capture

CHATBOT_URL = 'http://localhost:8082/uploadimage'

def execute_intent(entities):
    image_file = capture()
    files = {'file': open(image_name)}
    response = requests.post(CHATBOT_URL, files=files)
    return 'Done! The image has successfully been sent to your mobile device'
