"""
LICENSE:
===============

    Copyright (c) 2018 Marita Fitzgerald and the Creative Science Foundation. All rights reserved.
    Copyright (c) 2014-2017, Anthony Zhang <azhang9@gmail.com> All rights reserved.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    DEPENDENCIES:
    ===============
    install using pip commands:
    pip install PyAudio
    pip install SpeechRecognition

    QUICK TUTORIAL GOOGLE SPEECH:
    ===============

    1.Ensure you import the class from this module at the top of your python file as below:
    from codeelisten import CodeeListen

    2.Create an instance of CodeeListen as below:
    listen = CodeeListen()

    3.Use the get_speech_text() function to get the recognised text as below
    User Words = listen.get_speech_text()

    QUICK TUTORIAL WIT.AI:
    ======================

    1.Visit wit.ai and sign up for a free account, create app and get api key

    2.Ensure you import the class from this module at the top of your python file as below:
    from codeelisten import CodeeListenWit

    3.Create an instance of CodeeListen as below:
    listen = CodeeListen()

    3.Use the get_speech_text() function to get the recognised text as below
    User Words = listen.get_speech_text()

    NOTES
    =====
    * Google Speech is generally quicker than Wit, though occasionally throws Bad Gateway errors.
"""


import speech_recognition as sr

class CodeeListen:

    def get_speech_text(self):
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Error: Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return "Error: Could not request results from Google Speech Recognition; {0}".format(e)


class CodeeListenWit:

    def WIT_AI_KEY(self):
        return "<Insert API Key from Wit.ai>"

    def get_speech_text_wit(self, wit):
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            return r.recognize_wit(audio, key=wit)
        except sr.UnknownValueError:
            return "Wit.ai could not understand audio"
        except sr.RequestError as e:
            return "Could not request results from Wit.ai service; {0}".format(e)
