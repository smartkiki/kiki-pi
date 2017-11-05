import os

VOICE = 'Lekha'
COMMAND_STRING = 'say -v {} {}'.format(VOICE)


def speak(message):
    command = COMMAND_STRING.format(message)
    os.system(command)
