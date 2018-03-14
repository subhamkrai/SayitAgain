#!/usr/bin/env python

import speech_recognition as sr
from termcolor import colored as color
import apiai
import json
from os import system
import wikipedia as wiki
from time import sleep
import webbrowser as wb


BOLD = "\033[1m"   #use to bold the text
END = "\033[0m"    #use to close the bold text
CLIENT_ACCESS_TOKEN = "ddc70981eb8e4288aabeb842a40563ed"
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

try:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		system("clear")
        	print color(BOLD+"Hola!\nAsk me anything."+END,"red")
		while True:        
			audio = r.listen(source)


#	while True:	
			try:
				query = r.recognize_google(audio)
				print color(BOLD+"You said "+query+END+"\n","blue")
				request = ai.text_request()
				request.query = query  
				response = request.getresponse()
				json_data = (response.read())
	    			say =  json.loads(json_data)
				speech = say['result']['fulfillment']['speech']
				search = speech.split(":")
				if search[0] == "Google" :
					wb.open_new_tab("https://www.google.com/search?q="+search[1]+"")
				elif search[0] == "Wiki" :
					wiki_say = wiki.summary(search[1])
					print color(BOLD+"                               "+wiki_say+END+"\n","green")
				else :
					print color(BOLD+"                               "+speech+END+"\n","green")
				sleep(3)
				
			except sr.UnknownValueError:
				print color("Why you stopped talking to me?","blue")

except KeyboardInterrupt:
	print color(BOLD+" Bye!"+END, "cyan")
