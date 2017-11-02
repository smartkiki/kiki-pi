#alarm service
import datetime
import os


def alarm_process(time):
	print "\ntime is this"
	print time
	al_t = time.strftime("%I:%M %p")
	stop = False
	alarm_time = str(time)
	while stop == False:
		rn = str(datetime.datetime.now().time())
		if rn >= alarm_time:
			stop = True
			os.system("say -v Daniel 'Hi this is Kiki reminding you that it is %s'" % al_t)