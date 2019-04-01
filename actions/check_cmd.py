from time import localtime, strftime
from pygame import mixer
import pyscreenshot as ImageGrab
import pyaudio
import sys
import os
import random
import socket
import webbrowser
import subprocess
import glob
import time
import requests

from actions import check_audio
from actions import mail
from actions import youtube
import file_search
from actions import screenshot
from Voice import speakmodule
from Ears import ears



class CheckCommand():

    doss = os.getcwd()
    i=0
    
    def random_text(self,rand):
        text = random.choice(rand)
        return text

    def check(self,message,mode):
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
            print("i am here")
            rand = ['Wellcome to Jarvis virtual intelligence System. At your service sir.',
            'Hi, How are You?','At your service sir']
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            time.sleep(5)
            return True

        if ('thanks') in message or ('tanks') in message or ('thank you') in message:
            rand = ['You are wellcome', 'no problem',"With Pleasure,Sir",
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


        if ('wi-fi') in message or ("check wi-fi") in message:  
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
            

        if ('google maps') in message or ('google map') in message or ('maps') in message or ('map') in message:
            query = message
            stopwords = ['google', 'maps','map']
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
            print(result)
            rand = [('installing '+result)]
            msg = self.random_text(rand)
            check_audio.check(msg)
            #speakmodule.speak(rand,n,mixer)
            os.system('python -m pip install ' + result)
            return True

        if ('music') in message:
            rand = ['playing music']
            msg = self.random_text(rand)
            dirname = os.path.dirname(__file__)
            if mode == "text":
                name = input("Enter File Name To Be Played\n")
                found = file_search.search(name)
                path=r"/root/Desktop/Jarvis/music/"+name.lower()+".mp3"
                if found :
                    filename = os.path.join(dirname,path)
                    check_audio.check(msg)
                    #speakmodule.speak(rand,n,mixer)
                    time.sleep(6)

                    mixer.init()
                    mixer.music.load(filename)
                    mixer.music.play()
                    time.sleep(5)
                    return True
                else:
                    check_audio.check(msg)
                    youtube.play(name)
                    return True
            if mode == "voice":
                ok = True
                while ok :
                    name=ears.listen("Say Music Name")
                    name=name.replace(" ","")
                    confirm = input("Confirm Command Y/N \n")
                    if confirm =='Y' or confirm == 'y':
                        ok=False
                found = file_search.search(name)
                path=r"/root/Desktop/Jarvis/music/"+name.lower()+".mp3"
                if found :
                    filename = os.path.join(dirname,path)
                    check_audio.check(msg)
                    #speakmodule.speak(rand,n,mixer)
                    time.sleep(6)

                    mixer.init()
                    mixer.music.load(filename)
                    mixer.music.play()
                    time.sleep(5)
                    return True
                else:
                    check_audio.check(msg)
                    youtube.play(name)
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
            os.system("/sbin/shutdown now")
            return True

        if ('restart') in message:
            os.system("/sbin/shutdown -r now")
            return True
            
           
        if ('what time') in message:
            tim = strftime("%X", localtime())
            rand = [tim]
            msg = self.random_text(rand)
            #check_audio.check(msg)
            speakmodule.speak(rand,n,mixer)
            return True

        if ("send mail") in message:
            # ok = True
            # while ok :
            #     to=ears.listen("Say Receiver mail")
            #     to=to.replace(" ","")
            #     print(to)
            #     confirm = input("Confirm Command Y/N \n")
            #     if confirm =='Y' or confirm == 'y':
            #         break

            # while ok :
            #     msg=ears.listen("Say Message to se Send")
            #     #msg="".join(msg.replace(" ",""))
            #     confirm = input("Confirm Command Y/N \n")
            #     if confirm =='Y' or confirm == 'y':
            #         break
            # while ok :
            #     subject=ears.listen("Say Subject")
            #     confirm = input("Confirm Command Y/N \n")
            #     if confirm =='Y' or confirm == 'y':
            #         break

            to = input("Enter Receiver Mail\n")
            body = input("Write Message\n")
            subject = input("Enter Subject\n")

            rand =["sending mail","please wait sending your mail"]
            msg = self.random_text(rand)
            check_audio.check(msg)
            mail.send_mail(to,body,subject)

            msg = "Your Mail Is Sent"
            check_audio.check(msg)
            time.sleep(5)
            return True

        if ("take screenshot") in message:
            im=ImageGrab.grab()
            im.show()
            return True
        if ("search") in message:
            query = message
            stopwords = ['search']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            webbrowser.open("https://www.google.com/search?q="+result)
            return True

        if ("create file") in message :
            return True

        if ("create directory") in message :
            return True
        if ("copy file") in message :
            return True
        if ("move file") in message :
            return True
        if ("delete file") in message :
            return True
        if ("delete directory") in message :
            return True

