import sys, json, requests
from flask import Flask, request, jsonify
from nlp import response as nlp
from stt import speech_recognizer as stt
from services import intent_handler as ih
from services import toggle_service as ts
import os

app = Flask(__name__)
nlp_handler = nlp.Response()

def message_handler():
		"""
		This method deals with handling understanding and responding to user's request.
		"""

		# get the user's input and store in user_input variable.
		while True:
			user_input = stt.wait_for_input()
			"""
			TEXT PROCESSING CODE
			Parses text and returns response string.
			"""
			responseText = nlp_handler.get_response(user_input)
			
			#Removing single quotes in output string and converting text to speech
			output = responseText #.translate(str) #.maketrans({"'":None}))
			os.system("say -v Daniel '%s'" % output)



#message_handler()


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
		intent, entities = "weather", "West Lafayette" #nlp_handler.get_intent(message)
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
		os.system("say -v Daniel '%s'" % mess)
		resp = {"message" : mess}
		resp['statusCode'] = "200"
		print "sending the following back:"
		print resp
		return jsonify(resp)