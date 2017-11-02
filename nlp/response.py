import sys, json, requests
from flask import Flask, request
import os

CLIENT_ACCESS_TOKEN = 'f938c1b9f7b4467ebbde42c46d8338a6'

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

class Response(object):
	"""
	An object responsible for all recast related functionality
	"""

	def get_response(self, user_req):
		# Client Access Token for accessing our API AI Bot
		# I'll put the token in a common vars file in the next commit.

		# An endpoint to ApiAi, an object used for making requests to a particular agent.

		# Ranga/eeps text goes here.
		request = ai.text_request()
		request.query = user_req

		# Receiving the response.
		response = json.loads(request.getresponse().read().decode('utf-8'))
		responseStatus = response['status']['code']
		parsedString = ""
		if (responseStatus == 200):
			parsedString = response['result']['fulfillment']['speech']

		else:
			parsedString = "Sorry, I didn't get you."

		return parsedString

	def get_intent(self, user_req):
		#Edla please get intent and entities and send them both as follows:
		# return intent, entities <- here entities is an array of entities
		request = ai.text_request()
		request.query = user_req

		# Receiving the response.
		response = json.loads(request.getresponse().read().decode('utf-8'))
		responseStatus = response['status']['code']
		print response

		if (responseStatus == 200):
			intent = response['result']['metadata']['intentName']
			entities = []

			for i in response['result']['parameters']['location']:
				entities.append(response['result']['parameters']['location'][i])

		return intent, entities
		
