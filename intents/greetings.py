import random


GREETINGS = [
	'Hi! How are you today?',
	'hello! hope you are having a great day',
	'guess this starts the demo then! Hi I am Kiki at your service',
	'good day to you too!',
	'how may I help you today?',
	'great day today right?'
]


def execute_intent(entities):
	return random.choice(GREETINGS)