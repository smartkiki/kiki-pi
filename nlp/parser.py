import apiai
import simplejson as json


CLIENT_ACCESS_TOKEN = 'f938c1b9f7b4467ebbde42c46d8338a6'
DEFAULT_RESPONSE_STRING = "Sorry I didn't get that"
DEFAULT_INTENT = None
DEFAULT_ENTITIES = None

ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)


def get_response(user_req):
    request = _create_request(user_req)
    response = json.load(request.getresponse())
    response_string = _parse_response_string(response)

    return response_string


def get_intent(user_req):
    request = _create_request(user_req)
    response = json.load(request.getresponse())

    response_string = _parse_response_string(response)
    intent = _parse_intent(response)
    entities = _parse_entities(response)

    return response_string, intent, entities


def _create_request(user_req):
    request = ai.text_request()
    request.query = user_req

    return request


def _parse_response_string(response):
    status = response['status']['code']

    if status is 200:
        parsed_response = response['result']['fulfillment']['speech']
    else:
        parsed_response = DEFAULT_RESPONSE_STRING

    return parsed_response


def _parse_intent(response):
    status = response['status']['code']

    if status is 200:
        parsed_intent = response['result']['metadata']['intentName']
    else:
        parsed_intent = DEFAULT_INTENT

    return parsed_intent


def _parse_entities(response):
    status = response['status']['code']

    if status is 200:
        parsed_entities = response['result']['parameters']
    else:
        parsed_entities = DEFAULT_ENTITIES

    return parsed_entities
