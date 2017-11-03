from datetime import datetime
import os
import tempfile


COMMAND_STRING = "raspistill -o {}"
IMAGE_FILE = 'image.jpg'


def capture():

    command = COMMAND_STRING.format(IMAGE_FILE)
    os.system(command)

    return IMAGE_FILE

