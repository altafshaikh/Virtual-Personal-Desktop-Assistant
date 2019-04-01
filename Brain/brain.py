from pygame import mixer
import speech_recognition as sr
import os
import time
import requests
import json

from actions.check_cmd import CheckCommand
from actions import check_audio
from Voice import speakmodule


dirname = os.path.dirname(__file__)
#change this if you are using windows
path=r"/root/Desktop/Jarvis/audio/"
filename=''


class Brain():

	def print_welcome(self):
		
		welcome_message =  """
	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	+++++++++++++++++++++  Welcome to V.P.D.A  +++++++++++++++++++++
	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	+                                                              +
	+           I am J.A.R.V.I.S, How can I help You!              +
	+                                                              +
	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			"""
		print (welcome_message)
		msg = "Hello, I am jarvis How can i help you"
		check_audio.check(msg)

	def text_mode(self):
		mode="text"
		self.print_welcome()
		msg="At Your Service Sir"
		check_audio.check(msg)
		CC = CheckCommand()
		while 1:
			cmd = input("> ")
			#print(cmd)
			task = CC.check(cmd,mode)
			if task == True:
				msg="What else i can do for you"
				#check_audio.check(msg)
				print(msg)
			if task == False:
				msg="Task is Not Complete, Please Can U Say it Again!"
				#check_audio.check(msg)
				print(msg)
			
	def voice_mode(self):
		mode = "voice"
		self.print_welcome()
		msg="At Your Service Sir"
		check_audio.check(msg)
		CC = CheckCommand()

		while 1:
			r = sr.Recognizer()
			with sr.Microphone() as source:
				audio = r.adjust_for_ambient_noise(source) 
				print("Say something!")
				audio = r.listen(source)
				#print(audio)

			try:
				s = (r.recognize_google(audio))
				message = (s.lower())
				print (message)
				task=CC.check(message,mode)
				if task == True:
					msg="What else i can do for you"
					#check_audio.check(msg)
					print(msg)
				if task == False:
					msg="Task is Not Complete, Please Can U Say it Again!"
					#check_audio.check(msg)
					print(msg)


			except sr.UnknownValueError:
				print("$could not understand audio")
			except sr.RequestError as e:
				print("Could not request results$; {0}".format(e))
		
	def remote_mode(self):
		mode = "remote"
		self.print_welcome()
		msg="fetching remote command"
		check_audio.check(msg)
		CC = CheckCommand()
		
		print("Fetching Commands.......")
		while 1:
			r = requests.get('http://localhost:8000/commands/webapp/')
			response=json.loads(r.text)
					
			if response :
				print("Commands fetched")
				for cmd in response :
					if cmd['done'] == 'false':
						# commands.append(cmd['task'])
						cmmd = cmd['task']
						print(cmmd)
						done = CC.check(cmmd,mode)
						#time.sleep(15)
						if done == True:
							msg="Executing Next command"
							#check_audio.check(msg)
							print(msg)
							cmd['done'] ="true"
							r = requests.put('http://localhost:8000/commands/webapp/'+str(cmd['id'])+'/', json=cmd)
							time.sleep(5)
							#self.remote_mode()

						if done == False:
							msg="Task is Not Complete, Please Can U Say it Again!"
							#check_audio.check(msg)
							print(msg)



				






		

	
		
		
		
	
		
  
	
