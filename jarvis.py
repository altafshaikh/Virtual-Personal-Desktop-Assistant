from Brain.brain import Brain
import subprocess
import sys
from pygame import mixer
from Voice import speakmodule
#from sql_lite import Connection
import os
#import my_sqlite as sq

# execute_query = Connection()
# conn = execute_query.connect()
# execute_query.create_table(conn)
# dirname = os.path.dirname(__file__)
#change this if you are using windows
# path=r"/root/Desktop/Jarvis/audio/"
# filename=''
# sq.create_table()


def main():
	mode=[]
	try:
		mode = sys.argv
		if mode[1][1:]=="text":
			msg="Initializing Text Mode"
			#print(msg)
			
			#audio_path = sq.select(msg)
			# audio_path=[]
			
			# if audio_path:
			# 	temp = path+msg+str(len(msg[0:]))+'.mp3'
			# 	filename = os.path.join(dirname,temp) 
			# 	#print(filename)
			# 	flag= sq.insert(msg,filename)
			# 	speakmodule.speak([msg],len(msg[0:]),mixer)
			# 	print(msg)
			# 	start_text_prompt()
			# else:
				# speakmodule.paly(audio_path,mixer)
				# print(msg)
				# start_text_prompt()
			speakmodule.speak([msg],len(msg[0:]),mixer)
			#print(msg)
			start_text_prompt()

				
				

		if mode[1][1:]=="voice":
			#print("Initializing Voice Mode")
			msg="Initializing Voice Mode"
			speakmodule.speak([msg],len(msg[0:]),mixer)
			start_listening()

		if mode[1][1:]=="remote":
			#print("Initializing Remote Mode")
			msg="Initializing Remote Mode"
			speakmodule.speak([msg],len(msg[0:]),mixer)
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
	
	
