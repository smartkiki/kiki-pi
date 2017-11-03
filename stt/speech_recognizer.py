import speech_recognition as sr
import os, signal

def wait_for_input():
    r = sr.Recognizer()
    m = sr.Microphone()

    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
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

def signal_handler(sig, frame):
    print '\n\nYou pressed Ctrl+C! in speech recognizer\n\n'
    curr = os.getpid()
    #parent = os.getppid()
    os.kill(curr, signal.SIGKILL)
    #os.kill(parent, signal.SIGKILL)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)