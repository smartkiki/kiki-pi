import weather
import alarm
import take_image
import object_recognition
import default

INTENT_MAP = {
    'weather': weather,
    'alarm': alarm,
    'take_image': take_image,
    'object_recognition': object_recognition,
}


def handle_intent(intent, entities):
    handler = INTENT_MAP.get(intent, default)
    return handler.execute_intent(entities)
