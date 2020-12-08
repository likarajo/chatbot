# Functionalities

## Talk

* Pass audio as an argument to let the bot talk.
* Use gTTS to convert all the texts to speech.
* Once loop finished, save result to file.
* Initialize pygame.mixer and then load and play the audio file.

## Get User Input

* Use SpeechRecognition library with PyAudio package to recognize speech data.
* Capture input from the microphone as source using the listen() method of the Recognizer class.
* Record input from the source until silence is detected.

## Assistant

* Once the program is run the assistant will continue to listen for commands.
* On greeting the assistant will greet the user back.
* When the assistant does't get the command, it responds accordingly.

## Search in google

* The re.search() method takes a regular expression pattern and a string and searches for that pattern within the string. If the search is successful, search() returns a match object or None otherwise.
* The search is immediately followed by an if-statement to test if the search succeeded.
* The topic to be searched is extracted from the command and saved in a variable.
* Then the if-statement tests the match - if true the search succeeded and group() is the matching text. Otherwise if the match is false (None to be more specific), then the search did not succeed, and there is no matching text.
* The n in reg_ex.group(n) represents the nth parenthesized subgroup.

## Send email

* By default, Google does not allow logging in via smtplib because it is less secure. So less secure app access it has to be [enabled](https://myaccount.google.com/lesssecureapps) while being logged in to the google account.
* Obtain the subject, message, and recipient email address from user input
* init gmail SMTP
* identify the server
* encrypt session
* login to the server
* send the message
* end mail server connection
