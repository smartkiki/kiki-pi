import speech_recognition as sr
import os 

def wait_for_input():
    r = sr.Recognizer()
    m = sr.Microphone()

    try:
        print("A moment of silence, please...")
        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                value = r.recognize_google(audio)                
                if str is bytes:
                    print(u"You said {}".format(value).encode("utf-8"))
                else:
                    print("You said {}".format(value))
                return value
            except sr.UnknownValueError:
                return "SR_UVERR"
            except sr.RequestError as e:
                return "SR_RERR"
    except KeyboardInterrupt:
        pass