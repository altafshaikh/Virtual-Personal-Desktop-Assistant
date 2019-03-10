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


from Voice import speakmodule


class CheckCommand():

    doss = os.getcwd()
    i=0
    

    def check(self,message):
        n=len(message)
        
        if ('goodbye') in message:                          
            rand = ['Goodbye Sir', 'Jarvis powering off in 3, 2, 1, 0',
            'Bye']
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            time.sleep(5)
            sys.exit(1)
            
        if ('hello') in message or ('hi') in message:
            rand = ['Wellcome to Jarvis virtual intelligence project. At your service sir.',
            'Hi, How are You?']
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            time.sleep(5)
            return True

        if ('thanks') in message or ('tanks') in message or ('thank you') in message:
            rand = ['You are wellcome', 'no problem',"With Plesure,Sir",
            "Anytime at your service, sir"]
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            return True

        if message == ('jarvis'):
            rand = ['Yes Sir?', 'What can I do for you sir?']
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            return True

        if  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            rand = ['Fine thank you']
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            return True

        if  ('*') in message:
            rand = ['Be polite please']
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            return True

        if ('your name') in message:
            rand = ['My name is Jarvis, at your service sir','jarvis']
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            return True


        if ('wi-fi') in message:  
            REMOTE_SERVER = "www.google.com"
            speakmodule.wifi()
            rand = ['We are connected']
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            return True

        if ('.com') in message :
            rand = ['Opening' + message]         
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            webbrowser.get(Chrome).open('http://www.'+message)
            print ('')
            return True
            

        if ('google maps') in message:
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            rand = [result+'on google maps']
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            return True

        if message != ('start music') and ('start') in message:   
            query = message
            stopwords = ['start']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('start ' + result)
            rand = [('starting '+result)]
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            return True

        if message != ('stop music') and ('stop') in message:
            query = message
            stopwords = ['stop']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            rand = [('stopping '+result)]
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            return True

        if ('install') in message:
            query = message
            stopwords = ['install']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = [('installing '+result)]
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            os.system('python -m pip install ' + result)
            return True


        if ('sleep mode') in message:
            rand = ['good night']
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            return True

        if ('music') in message:
            mus = random.choice(glob.glob(doss + "\\music" + "\\*.mp3"))
            #os.system('chown -R user-id:group-id mus')
            os.system('start ' + mus)
            rand = ['start playing']
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            return True

        if ('what time') in message:
            tim = strftime("%X", localtime())
            rand = [tim]
            #rand=random.choice(rand)
            speakmodule.speak(rand,n,mixer)
            return True
