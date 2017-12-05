from recastai import Request


CLIENT_ACCESS_TOKEN = '5b6df69bc243a4318f6d097adc27d9cc'
DEFAULT_RESPONSE_STRING = "Sorry I didn't get that"
DEFAULT_INTENT = None
DEFAULT_ENTITIES = None

client = Request(CLIENT_ACCESS_TOKEN, 'en')

"""
def get_response(user_req):
    request = _create_request(user_req)
    response = json.load(request.getresponse())
    response_string = _parse_response_string(response)

    return response_string
"""


def get_intent(user_req):
    response = _send_request(user_req)
    intent = _parse_intent(response)
    entities = _parse_entities(response)

    return intent, entities


def _send_request(user_req):
    response = client.analyse_text(user_req)

    return response

def _parse_intent(response):
    if response.intent:
        parsed_intent = response.intent.slug
    else:
        parsed_intent = DEFAULT_INTENT

    return parsed_intent


def _parse_entities(response):
    if response.entities:
        parsed_entities = response.entities
    else:
        parsed_entities = DEFAULT_ENTITIES

    return parsed_entities
