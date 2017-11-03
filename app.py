from flask import Flask, request, jsonify
from nlp import response as nlp
from stt import speech_recognizer as stt
from services import intent_handler as ih
from services import toggle_service as ts
from multiprocessing import Process
import os

app = Flask(__name__)

nlp_handler = nlp.Response()


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/chatbot', methods=['POST'])
def get_message_from_chatbot():
    if not request.json:
        print "Didnt get a json request. Bad request"
        return str(404)
    else:
        print(request.json)
        json_request = request.json
        message = json_request['message']
        intent, entities = nlp_handler.get_intent(message)
        mess = ih.intent_handler(intent, entities)
        os.system("say -v Lekha '%s'" % mess)
        resp = {"message": mess}
        resp["statusCode"] = "200"
        print("sending the following back:")
        print(resp)
        return jsonify(resp)


@app.route('/postback', methods=['POST'])
def get_postback_prefrences():
    if not request.json:
        print("Didnt get a json request. Bad request")
        resp = {"message": "error. json wasnt sent", "statusCode": "400"}
        return jsonify(resp)
    else:
        print(request.json)
        mess = ts.toggle_service(request.json['payload_type'])
        print("\n\ntoggled service\n\n")
        os.system("say -v Lekha '%s'" % mess)
        resp = {"message": mess}
        resp['statusCode'] = "200"
        print("sending the following back:")
        print(resp)
        return jsonify(resp)


def message_handler():
    while True:
        p = os.getpid()
        print "pid which starts off the listening functionality: %d\n\n" % p
        user_input = stt.wait_for_input()
        intent, entities, mess = nlp_handler.get_intent(user_input)

        if intent != "Greeting":
            mess = ih.intent_handler(intent, entities)

        # Removing single quotes in output string and converting text to speech
        output = mess
        print("\n\n output is : %s \n\n" % output)
        output.replace("'", "")
        print("\n\n output is : %s \n\n" % output)
        os.system("say -v Lekha '%s'" % output)


if __name__ == '__main__':

    p = Process(target=message_handler, args=())
    p.start()
    app.run(debug=True, use_reloader=False)
