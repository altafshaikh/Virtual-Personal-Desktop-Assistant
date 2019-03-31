import subprocess
import sys
from pygame import mixer
import os
import time

from Brain.brain import Brain
from MySqlite import mysqlite as sq
from Voice import speakmodule
from actions import check_audio

sq.create_table()


def main():
	mode=[]
	try:
		mode = sys.argv
		if mode[1][1:]=="text":
			msg="Initializing Text Mode"
			check_audio.check(msg)
			start_text_prompt()

		if mode[1][1:]=="voice":
			msg="Initializing Voice Mode"
			check_audio.check(msg)
			start_listening()

		if mode[1][1:]=="remote":
			msg="Initializing Remote Mode"
			check_audio.check(msg)
			start_remote_prompt()

	except IndexError:
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
	
	
