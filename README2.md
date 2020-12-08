# My Virtual Assistant

## Dependencies

```sh
# Install package for device audio
brew install portaudio

# Create a virtual environment and activate it (optional)
pip3 install virtualenv
virtualenv venv
. venv/bin/activate

#Install the required libraries
pip3 install -r requirements2.txt

#Install certificates
python3 util/install_certify.py
```

On macOS run **install_certificates.command**

* **gTTS (Google Text-to-Speech)**: Python library and CLI tool to interface with ***Google Translate***'s *text-to-speech* API. This module helps to convert String text to Spoken text and can be saved as .mp3.

* **SpeechRecognition**: To retrieve speech input and process audio files. The Google Web Speech API supports a default API key that is hard-coded into the SpeechRecognition library

* **PyAudio**: To access the microphone.

* **pygame**: A cross-platform set of Python modules containing computer graphics and sound libraries.

* **webbrowser**: (built-in package) To display Web-based documents.

* **re**: (built-in package) Regular expressions to detect availability of user commands by matching them.

* **smtplib**: (built-in package) To send emails by communicating with mail servers via Simple Mail Transfer Protocol (SMTP).

* **requests**: To access HTTP API.

* **bs4**: Beautiful Soup 4, to pull data out of HTML and XML files.

* **urllib**: (built-in package) To access any URL

---

## [Functionalities](files/functionalities.md)

* Talk
* Get User Input
* Assistant (perform tasks)
* Search Google
* Send email
* Search wikipedia
