from google import search
import requests

CHATBOT_URL = 'http://localhost:8082/searchresults'

FOUND_RESULTS = "I found a few results that I sent to your mobile device!"
NOT_FOUND = "Could not understand the query. Please try again."


def execute_intent(entities):
	for e in entities:
		if e.name == 'search_query':
			query = e.value
			break
	if query:
		results_array = search(query, tld='com', num=5, stop=1, pause=2)
		data = _create_json_for_request(results_array)
		r = requests.post(CHATBOT_URL, json=data)
		return FOUND_RESULTS
	else:
		return NOT_FOUND 


def _create_json_for_request(results):
	arr = []
	for r in results:
		arr.append(str(r))
	data = { 
		"fbid" : "1725030900888096",
		"urls" : arr
		}
	return data