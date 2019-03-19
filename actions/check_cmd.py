from time import localtime, strftime
from pygame import mixer
import pyaudio
import sys
import os
import random
import socket
import webbrowser
import subprocess
import glob
import time

from actions import check_audio
from actions import mail
from Voice import speakmodule


class CheckCommand():

    doss = os.getcwd()
    i=0
    
    def random_text(self,rand):
        text = random.choice(rand)
        return text

    def check(self,message):
        n=len(message)
        if ('goodbye') in message:                          
            rand = ['Goodbye Sir', 'Jarvis powering off in 3, 2, 1, 0',
            'Bye']
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            time.sleep(5)
            sys.exit(1)
            
        if ('hello') in message or ('hi') in message:
            rand = ['Wellcome to Jarvis virtual intelligence System. At your service sir.',
            'Hi, How are You?','At your service sir']
            msg = self.random_text(rand)
            print("mein idhar hu")
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            time.sleep(5)
            return True

        if ('thanks') in message or ('tanks') in message or ('thank you') in message:
            rand = ['You are wellcome', 'no problem',"With Plesure,Sir",
            "Anytime at your service, sir"]
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            return True

        if message == ('jarvis'):
            rand = ['Yes Sir?', 'What can I do for you sir?']
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            return True

        if  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            rand = ['Fine thank you','Fine sir']
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            return True

        if  ('*') in message:
            rand = ['Be polite please']
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            return True

        if ('your name') in message:
            rand = ['My name is Jarvis, at your service sir','jarvis']
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            return True


        if ('wi-fi') in message:  
            REMOTE_SERVER = "www.google.com"
            speakmodule.wifi()
            rand = ['We are connected']
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            return True

        if ('.com') in message :
            rand = ['Opening' + message]         
            #Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            #cross platform
            webbrowser.open('http://www.'+message)
            print ('')
            return True
            

        if ('google maps') in message:
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            webbrowser.open("https://www.google.be/maps/place/"+result+"/")
            rand = [result+'on google maps']
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            return True

        if ('install') in message:
            query = message
            stopwords = ['install']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = [('installing '+result)]
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            os.system('python -m pip install ' + result)
            return True

        if ('music') in message:
            dirname = os.path.dirname(__file__)
            #change this if you are using windows
            path=r"/root/Desktop/Jarvis/music/NaJa.mp3"
            filename = os.path.join(dirname,path) 

            rand = ['playing music']
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            time.sleep(6)

            mixer.init()
            mixer.music.load(filename)
            mixer.music.play()
            time.sleep(5)
            #print("mein idhar hu")
            return True

        if ('pause') in message:
            mixer.music.pause()
            return True

        if ('stop') in message:
            mixer.music.stop()
            return True

        if ('resume') in message:
            mixer.music.unpause()
            return True

        if ('shutdown') in message:
            os.system("shutdown /s /t 1")
            return True

        if ('restart') in message:
            os.system("shutdown /r /t 1")
            return True
            
           
        if ('what time') in message:
            tim = strftime("%X", localtime())
            rand = [tim]
            msg = self.random_text(rand)
            #check_audio.check(msg)
            speakmodule.speak(rand,n,mixer)
            return True

        if ("send mail") in message:
            to = input("Enter Receiver Mail")
            msg = input("Write Message")
            subject = input("Enter Subject")

            rand =["sending mail","please wait sending your mail"]
            msg = self.random_text(rand)
            check_audio.check(msg)
            mail.send_mail(to,msg,subject)

            msg = "Your Mail Is Sent"
            check_audio.check(msg)
            time.sleep(5)
            return True

        #if ('sleep mode') in message:
        #     rand = ['good night']
        #     msg = self.random_text(rand)
        #     check_audio.check(msg)
        #     #speakmodule.speak(rand,n,mixer)
        #     os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        #     return True

                # if message != ('start music') and ('start') in message:   
        #     query = message
        #     stopwords = ['start']
        #     querywords = query.split()
        #     resultwords  = [word for word in querywords if word.lower() not in stopwords]
        #     result = ' '.join(resultwords)
        #     dirname = os.path.dirname(__file__)
        #     #change this if you are using windows
        #     path=r"/root/Desktop/Jarvis/music/"+result+".mp3"
        #     filename = os.path.join(dirname,path) 
        #     rand = [('starting '+result)]
        #     msg = self.random_text(rand)
        #     check_audio.check(msg)
        #     #speakmodule.speak(rand,n,mixer)

        #     time.sleep(5)
        #     mixer.init()
        #     mixer.music.load(filename)
        #     mixer.music.play()
        #     return True

        # if message != ('stop music') and ('stop') in message:
        #     query = message
        #     stopwords = ['stop']
        #     querywords = query.split()
        #     resultwords  = [word for word in querywords if word.lower() not in stopwords]
        #     result = ' '.join(resultwords)
        #     os.system('taskkill /im ' + result + '.exe /f')
        #     rand = [('stopping '+result)]
        #     msg = self.random_text(rand)
        #     check_audio.check(msg)
        #     #speakmodule.speak(rand,n,mixer)
        #     return True
