import sys, json, requests
from flask import Flask, request
from nlp import response as nlp
from stt import speech_recognizer as stt
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
			os.system("say '%s'" % output)



message_handler()


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/chatbot', methods=['POST'])
def get_message_from_chatbot():
	if not request.json:
		print "Didnt get a json request. Bad request"
	else:
		print request.json
		json_request = json.dumps(request.json)
		print json_request
	print "got to get message from chatbot"