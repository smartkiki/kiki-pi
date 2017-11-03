import sys, json, requests, signal
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
		print request.json
		json_request = request.json
		message = json_request['message']
		intent, entities = "weather", "Cuba" #nlp_handler.get_intent(message)
		mess = ih.intent_handler(intent, entities)
		os.system("say -v Daniel '%s'" % mess)
		resp = {"message" : mess}
		resp["statusCode"] = "200"
		print "sending the following back:"
		print resp
		return jsonify(resp)


@app.route('/postback', methods=['POST'])
def get_postback_prefrences():
	if not request.json:
		print "Didnt get a json request. Bad request"
		resp = {"message" : "error. json wasnt sent", "statusCode" : "400"}
		return jsonify(resp)
	else:
		print request.json
		mess = ts.toggle_service(request.json['payload_type'])
		print "\n\ntoggled service\n\n"
		os.system("say -v Daniel '%s'" % mess)
		resp = {"message" : mess}
		resp['statusCode'] = "200"
		print "sending the following back:"
		print resp
		return jsonify(resp)


def message_handler():
	while True:
		"""vol = os.system("osascript -e 'get input volume of (get volume settings)'")
		if vol == 0:
		continue"""
		p = os.getpid()
		print "pid which starts off the listening functionality: %d\n\n" % p
		user_input = stt.wait_for_input()
		"""
		TEXT PROCESSING CODE
		Parses text and returns response string.
		"""
		responseText = nlp_handler.get_response(user_input)
			
		#Removing single quotes in output string and converting text to speech
		output = responseText #.translate(str) #.maketrans({"'":None}))
		print "\n\n output is : %s \n\n" % output
		output.replace("'", "")
		print "\n\n output is : %s \n\n" % output
		os.system("say -v Daniel '%s'" % output)

def signal_handler(signal, frame):
    print '\n\nYou pressed Ctrl+C!\n\n'
    curr = os.getpid()
    print "parent pid : %d" % curr
    for p in processes:
    	p.terminate()
    sys.exit(0)

processes = []

p = Process(target=message_handler, args=())
processes.append(p)
p.start()
print "\n\n started another process with process name: %s\n process pid: %d \n\n" % (p.name, p.pid)
app.run(debug=True, use_reloader=False)
#p.join()
signal.signal(signal.SIGINT, signal_handler)
