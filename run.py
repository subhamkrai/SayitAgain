#!/usr/bin/env python

import speech_recognition as sr
from termcolor import colored as color
import apiai
import json
from os import system
import wikipedia as wiki

BOLD = "\033[1m"   #use to bold the text
END = "\033[0m"    #use to close the bold text
CLIENT_ACCESS_TOKEN = "ddc70981eb8e4288aabeb842a40563ed"
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
request = ai.text_request()

try:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		system("clear")
        	print color(BOLD+"Hola!\nAsk me anything."+END,"red")
        	audio = r.listen(source)


	while True:	
		try:
        		query = r.recognize_google(audio)
			print("You said "+query)
			request.query = query  
			response = request.getresponse()
			json_data = (response.read())
    			say =  json.loads(json_data)
    			print(say['result']['fulfillment']['speech'])      	

		except sr.UnknownValueError:
        		print("I could not understand this audio")

except KeyboardInterrupt:
	print("		Bye!")
