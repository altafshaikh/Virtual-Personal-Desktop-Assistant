from pygame import mixer
from Voice import speakmodule
from actions.check_cmd import CheckCommand
import speech_recognition as sr
#from Ears.ears import Ears


class Brain():

	# def __init_(self):
	# 	self.print_welcome()

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
		speakmodule.speak([msg],len(msg[0:]),mixer)

	def text_mode(self):
		self.print_welcome()
		msg="At Your Service Sir"
		speakmodule.speak([msg],len(msg[0:]),mixer)
		CC = CheckCommand()
		while 1:
			cmd = input("> ")
			print(cmd)
			task = CC.check(cmd)
			if task == True:
				print("What else i can do for you")
			if task == False:
				print("Task is Not Complete, Please Can U type it Again!")
			
	def voice_mode(self):
		self.print_welcome()
		msg="At Your Service Sir"
		speakmodule.speak([msg],len(msg[0:]),mixer)
		CC = CheckCommand()

		while 1:
			#cmd = ears.listen()
			r = sr.Recognizer()
			with sr.Microphone() as source:
				audio = r.adjust_for_ambient_noise(source) 
				print("Say something!")
				audio = r.listen(source)
				print(audio)

			try:
				s = (r.recognize_google(audio))
				message = (s.lower())
				print (message)
				task=CC.check(message)
				if task == True:
					#print("What else i can do for you")
					msg="What else i can do for you"
					speakmodule.speak([msg],len(msg[0:]),mixer)
				if task == False:
					#print("Task is Not Complete, Please Can U Say it Again!")
					msg="Task is Not Complete, Please Can U Say it Again!"
					speakmodule.speak([msg],len(msg[0:]),mixer)

	
			except sr.UnknownValueError:
				print("$could not understand audio")
			except sr.RequestError as e:
				print("Could not request results$; {0}".format(e))
		
	def remote_mode(self):
		pass
		self.print_welcome()
		

	
		
		
		
	
		
  
	
