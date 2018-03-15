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

google_search = "https://www.google.com/search?q="
youtube_search = "https://www.youtube.com/results?search_query="
google_drive = "https://drive.google.com"
gmail = "https://mail.google.com"

try:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		system("clear")
        	print color(BOLD+"Hola!\nAsk me anything."+END,"green")
		while True:        
			audio = r.listen(source)


#	while True:	
			try:
				query = r.recognize_google(audio)
			
				print color("                               "+BOLD+query+END+"\n","red")
				request = ai.text_request()
				request.query = query  
				response = request.getresponse()
				json_data = (response.read())
    				say =  json.loads(json_data)
				speech = say['result']['fulfillment']['speech']
				search = speech.split(":")
				if search[0] == "Google" or search[0] == "Google and Google":
					wb.open_new_tab(google_search+search[1])
					print()
				elif search[0] == "Wiki" :
					try:
						wiki_say = wiki.summary(search[1])
						print color(BOLD+wiki_say+END+"\n","green")
					except wiki.exceptions.DisambiguationError:
						print color(BOLD+"Try to google it because it is very confusing for me"+END,"red")
				elif search[0] == "Youtube":
					wb.open_new_tab(youtube_search+search[1])
					print("")
				elif search[0] == "Drive":
					wb.open_new_tab(google_drive)
					print("")
				elif search[0] == "Gmail":
					print("")
					wb.open_new_tab(gmail)
				else :
					print color(BOLD+speech+END+"\n","green")
				
			except sr.UnknownValueError:
				print color("Listening","blue")

except KeyboardInterrupt:
	print color(BOLD+" Bye!"+END, "cyan")
