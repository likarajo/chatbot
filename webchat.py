import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from gtts import gTTS
import speech_recognition as sr
import aiml
from autocorrect import Speller
from flask import Flask, render_template, request

app = Flask(__name__) # set up web app

BRAIN_FILE="model/pretrained_model.dump" # pre-trained AIML model (brain file)
kernel = aiml.Kernel() # interface to the AIML interpreter
spell = Speller(lang='en') # object for spell-check

if os.path.exists(BRAIN_FILE):
    kernel.loadBrain(BRAIN_FILE) # load the content of the brain file
else:
    kernel.bootstrap(learnFiles="model/learning_files.aiml", commands="LEARN AIML") # load the content of the AIML files
    kernel.saveBrain(BRAIN_FILE) # save the learned model to the brain file

# set up UI
@app.route("/") 
def home():
    return render_template("home.html")

# set up GET API
@app.route("/get")
def get_bot_response():
    query = request.args.get('msg') # get the user input
    query = [spell(w) for w in (query.split())] # perform spell check on the user input
    message = " ".join(query) # prepare the message
    response = kernel.respond(message) # get response for the message
    if response:
        return (str(response))
    else:
        return (str(":)"))

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port='5000') #host defaults to 127.0.0.1 (localhost). Set to 0.0.0.0 to have server available externally