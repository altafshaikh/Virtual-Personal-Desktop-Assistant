import speech_recognition as sr

	
def listen(msg):
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.adjust_for_ambient_noise(source) 
		print(msg)
		audio = r.listen(source)
		print(audio)

	try:
		s = (r.recognize_google(audio))
		message = (s.lower())
		print (message)
		return(message)

	except sr.UnknownValueError:
		print("$could not understand audio")
	except sr.RequestError as e:
		print("Could not request results$; {0}".format(e))
