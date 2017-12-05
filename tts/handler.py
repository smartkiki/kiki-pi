import os

VOICE = 'Daniel'
COMMAND_STRING = 'say -v {} {}'


def speak(message):
    command = COMMAND_STRING.format(VOICE, message)
    os.system(command)
