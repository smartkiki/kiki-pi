#toggle service
import os, sys

def toggle_service(payload_text):
	print "got to toggle service"
	message = ""
	if payload_text == "new_user":
		message = "Hello! Welcome to your Kiki chat interface! You can use the menu here to select toggle options or send messages from here to interact with your Kiki home AI!"
	elif payload_text == "SPEAKER_ON":
		#os.system("sudo amixer -c 0 cset numid=3 1 > /dev/null")
		os.system("osascript -e 'set volume 10'")
		message = "Speaker has been enabled"
	elif payload_text == "SPEAKER_OFF":
		os.system("osascript -e 'set volume 0'")
		message = "Speaker has been disabled"
	elif payload_text == "MIC_OFF":
		message = "Microphone has been disabled"
	elif payload_text == "MIC_ON":
		message = "Microphone has been enabled"
	return message