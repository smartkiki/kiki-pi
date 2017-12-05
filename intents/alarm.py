import datetime
import dateutil.parser
import os

from multiprocessing import Process


def execute_intent(entities):
    print(entities)
    for e in entities:
        if e.name == 'datetime':
            alarm_time = dateutil.parser.parse(e.iso)
    # alarm_time = datetime.datetime.strptime(time, '%H:%M:%S').time()
    print alarm_time
    p = Process(target=_alarm_process, args=(alarm_time,))
    p.start()
    return "Alright, I have set an alarm for %s" % alarm_time.strftime("%I:%M %p")


def _alarm_process(time):
    print type(time)
    al_t = time.strftime("%I:%M %p")
    stop = False
    alarm_time = str(time.time())
    while stop is False:
        rn = str(datetime.datetime.now().time())
        if rn >= alarm_time:
            stop = True
            os.system("say -v Daniel \
                'Hi this is Kiki reminding you that it is %s'" % al_t)
