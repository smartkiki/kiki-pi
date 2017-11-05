from ..camera.image_capture import capture


def execute_intent(entities):
    image_file = capture()
    return image_file
