from Brain.brain import Brain
import subprocess
import sys
from pygame import mixer
from Voice import speakmodule


def main():
	mode=[]
	try:
		mode = sys.argv
		if mode[1][1:]=="text":
			msg="Initializing Text Mode"
			speakmodule.speak([msg],len(msg[0:]),mixer)
			print(msg)
			start_text_prompt()

		if mode[1][1:]=="voice":
			print("Initializing Voice Mode")
			start_listening()

		if mode[1][1:]=="remote":
			print("Initializing Remote Mode")
			start_remote_prompt()

	except Exception:
		usage()

def start_listening():
	print("Voice Mode Activated")
	brain = Brain()
	brain.voice_mode()

	
def start_text_prompt():
	print("Text Input Mode Is Activated")
	brain = Brain()
	brain.text_mode()

def start_remote_prompt():
	print("Remote Mode Activated")
	brain = Brain()
	brain.remote_mode()

def usage():
	usage = """
	+-------------------------------------------------------+
	|   Usage: python jarvis.py [options]                   |
	|                                                       |
	|-------------------------------------------------------|
	|   -text     initialize jarvis with text mode.         |
	|   -voice    initialize jarvis with voice mode.        |
	|   -remote   initialize jarvis with remote mode.       |
	+-------------------------------------------------------+
	"""
	print (usage)
	sys.exit(1)

if __name__ == '__main__':
	main()
	
	
