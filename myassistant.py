import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from gtts import gTTS
import speech_recognition as sr
import random
import webbrowser
import re
import smtplib
import requests
import bs4
import urllib

errors = [
        "I don\'t understand what you said!",
        "Can you please repeat?",
        "Excuse me?",
        "I don\'t know what you mean!",
        "Sorry, I don\'t understand!"
    ] 

greetings = [
        "Hello! How can I help you?",
        "Hi there! What can I do for you?",
        "Hi!",
        "Hello!" 
    ]

def talk(text):
    print('BOT : ' + text + '\n')
    for line in text.splitlines():
        text2speech = gTTS(text=text, lang='en')
        text2speech.save('temp/audio.mp3')
        mixer.init()
        mixer.music.load('temp/audio.mp3')
        mixer.music.play()

def getInput():
    print('listening...')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('USER: ' + command + '\n')
        time.sleep(2)
    except sr.UnknownValueError:
        talk(random.choice(errors))
        time.sleep(3)
        command = getInput();
    return command    

def assistant(command):

    # Google Search
    if 'google' in command:
        regex = re.search('google (.*)', command)
        if regex:
            topic = regex.group(1)
            url = 'https://www.google.com/search?q=' + topic
        webbrowser.open(url)
        talk('Done!')
        time.sleep(3)

    # Send email
    elif 'send email' or 'gmail' in command:
        talk('What is the subject?')
        time.sleep(3)
        subject = getInput()
        talk('What is the message?')
        time.sleep(3)
        message = getInput()
        content = 'Subject: {}\n\n{}'.format(subject, message)
        #talk('What is the recipient email?')
        #time.sleep(3)
        #TO = getInput()
        TO = 'likarajo@gmail.com'
        FROM = 'likarajo@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('likarajo@gmail.com','rajarshich2007')
        server.sendmail(FROM, TO, content)
        server.close()
        talk('Email sent!')
        time.sleep(3)

    # Search Wikipedia
    elif 'wikipedia' in command:
        regex = re.search('wikipedia (.+)', command)
        if regex:
            topic = command.split("wikipedia",1)[1]
            response = requests.get("https://en.wikipedia.org/wiki/" + topic)
            if response is not None:
                html = bs4.BeautifulSoup(response.text, 'html.parser')
                title = html.select('#firstHeading')[0].text
                paragraphs = html.select('p')
                for para in paragraphs[0:5]:
                    print(para.text)
                intro = '\n'.join([para.text for para in paragraphs[0:2]])
                print(intro)
                t2s = gTTS(text=intro, lang='en', slow=False)
                t2s.save('temp/wiki.mp3')
                mixer.init()
                mixer.music.load('temp/wiki.mp3')
                mixer.music.play()
                while mixer.music.play():
                    time.sleep()

    # Search videos on Youtube and play
    elif 'youtube' in command:
        talk('Ok!')
        regex = re.search('youtube (.+)', command)
        if regex:
            domain = command.split("youtube",1)[1] 
            query_string = urllib.parse.urlencode({"search_query" : domain})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            #print("http://www.youtube.com/watch?v=" + search_results[0])
            webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
            pass

    # Greet
    elif 'hello' or 'hi' in command:
        talk(random.choice(greetings))
        time.sleep(3)

    # Enquire
    elif 'who are you' in command:
        talk('I am your virtual assistant')
        time.sleep(3)

    # Quit
    elif 'quit' or 'bye' in command:
        talk('Bye!')
        exit()

    # Stop
    elif 'stop' in command:
        mixer.music.stop()

    # Error 
    else:
        talk(random.choice(errors))
        time.sleep(3)

print('Welcome to your virtual assistant')
talk('I am ready!')
while True:
    time.sleep(4)
    assistant(getInput())
