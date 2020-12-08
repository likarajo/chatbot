import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from gtts import gTTS
import speech_recognition as sr
import aiml
from autocorrect import Speller
import random
import webbrowser
import re
import smtplib
import requests
import bs4
import urllib

error = False
action = False

def talk(text):
    for line in text.splitlines():
        text2speech = gTTS(text=text, lang='en')
        text2speech.save('temp/audio.mp3')
        mixer.init()
        mixer.music.load('temp/audio.mp3')
        mixer.music.play() 

def google_search(command):
    regex = re.search('google (.*)', command)
    if regex:
        topic = regex.group(1)
        url = 'https://www.google.com/search?q=' + topic
        webbrowser.open(url)
        error = False
    else:
        error = True

def wiki_search(command):
    regex = re.search('wikipedia (.+)', command)
    if regex:
        topic = regex.group(1)
        url = 'https://en.wikipedia.org/wiki/' + topic
        webbrowser.open(url)
        error = False
    else:
        error = True

def youtube(command):
    regex = re.search('youtube (.+)', command)
    if regex:
        domain = command.split("youtube",1)[1] 
        query_string = urllib.parse.urlencode({"search_query" : domain})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
        error = False
    else:
        error = True

#==============================================

def assistant(message):
    if 'google' in message:
        google_search(message)
        if error == True:
            action = False
        else:
            action = True

    elif 'wikipedia' in message:
        wiki_search(message)
        if error == True:
            action = False
        else:
            action = True

    elif 'youtube' in message:
        youtube(message)
        if error == True:
            action = False
        else:
            action = True

    else:
        action = False
    

BRAIN_FILE="model/pretrained_model.dump" # pre-trained AIML model

spell = Speller(lang='en') # object for spell-check

kernel = aiml.Kernel() # interface to the AIML interpreter
kernel._verboseMode = False

if os.path.exists(BRAIN_FILE):
    kernel.loadBrain(BRAIN_FILE) # load the content of the brain file
else:
    kernel.bootstrap(learnFiles="model/learning_files.aiml", commands="LEARN AIML") # load the content of the AIML files
    kernel.saveBrain(BRAIN_FILE) # save the model to brain file

print("Bot> ", "I am ready!")
talk("I am ready")

while True:
    userInput = input("User> ") # get user input
    if userInput.lower() in ('quit','exit'):
        exit()
    else:
        #query = [spell(w) for w in (userInput.split())] # perform spell check on the user input
        #message = " ".join(query) # prepare the message
        message = userInput
        assistant(userInput)
        if action:
            print("Bot> ", "Here you go!")
            talk("Here you go!")
        else:
            response = kernel.respond(message)
        if response:
            print("Bot> ", response)
            talk(response)
        else:
            print("Bot> :) ", )
        time.sleep(1)
    

    

    