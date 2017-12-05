import os

from multiprocessing import Process

from flask import Flask
from flask import request
from flask import jsonify

from nlp.parser import get_intent
from stt import speech_recognizer as stt
from tts import handler as tts
from intents import toggle_service as ts
from intents.handler import handle_intent

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/chatbot', methods=['POST'])
def get_message_from_chatbot():
    if not request.json:
        print("Didnt get a json request. Bad request")
        return str(404)
    else:
        print(request.json)
        json_request = request.json
        message = json_request['message']

        intent, entities = get_intent(message)
        message = handle_intent(intent, entities)
        tts.speak(message)

        response = {
            "message": message,
            "statusCode": 200,
        }

        print("sending the following back:")
        print(response)
        return jsonify(response)


@app.route('/postback', methods=['POST'])
def get_postback_prefrences():
    if not request.json:
        print("Didnt get a json request. Bad request")
        response = {
            "message": "error. json wasnt sent",
            "statusCode": "400",
        }
        return jsonify(response)
    else:
        print(request.json)
        message = ts.toggle_service(request.json['payload_type'])
        print("\n\ntoggled service\n\n")
        tts.speak(message)
        response = {
            "message": message,
            "statusCode": 200,
        }
        print("sending the following back:")
        print(response)
        return jsonify(response)


def message_handler():
    while True:
        p = os.getpid()
        print "pid which starts off the listening functionality: %d\n\n" % p
        user_input = stt.wait_for_input()
        intent, entities = get_intent(user_input)
        mess = handle_intent(intent, entities)

        # Removing single quotes in output string and converting text to speech
        output = mess
        print("\n\n output is : %s \n\n" % output)
        output.replace("'", "")
        print("\n\n output is : %s \n\n" % output)
        tts.speak(output)


p = Process(target=message_handler, args=())
p.start()
app.run(debug=True, use_reloader=False)
