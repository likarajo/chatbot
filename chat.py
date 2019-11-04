import os
import aiml
from autocorrect import Speller

BRAIN_FILE="model/pretrained_model.dump" # pre-trained AIML model

spell = Speller(lang='en') # object for spell-check

kernel = aiml.Kernel() # interface to the AIML interpreter

if os.path.exists(BRAIN_FILE):
    kernel.loadBrain(BRAIN_FILE) # load the content of the brain file
else:
    kernel.bootstrap(learnFiles="model/learning_files.aiml", commands="LEARN AIML") # load the content of the AIML files
    kernel.saveBrain(BRAIN_FILE) # save the model to brain file

while True:
    query = input("User> ") # get user input
    query = [spell(w) for w in (query.split())] # perform spell check on user input
    message = " ".join(query) # prepare the message
    response = kernel.respond(message) # get reponse for the message
    if response:
        print("Bot> ", response)
    else:
        print("Bot> :) ", )