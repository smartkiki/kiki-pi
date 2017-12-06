import os
import time

VOICE = 'en+f5 -s 155'
COMMAND_STRING = 'espeak -v {} {}'


def speak(message):
    command = COMMAND_STRING.format(VOICE, message)
    os.system(command)
