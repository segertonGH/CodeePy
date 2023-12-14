"""
LICENSE:
===============

    Copyright (c) 2018 Marita Fitzgerald and the Creative Science Foundation. All rights reserved.

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

    INSTRUCTIONS
    ============
    1. At the prompt choose from the following word commands and say them into your microphone
    - ARMS SWING
    - ARMS UP
    - ARMS DOWN
    - HEAD LOOK
    - HEAD STOP
    - SING
    - HAPPY
    - SAD
    - LOVE
    - STOP (stops all Codee's Movements)
    2. To exit say EXIT, QUIT or END

"""

import time
from codeepy import CodeePy
import speech_recognition as sr


def sad_tone():
    """
    This method makes codee play a sad sound
    """
    codee.play_notes_with_duration(["F4.1", "B3.1"])


def get_sr(question):
    """
    This method gets the speech recognition results
    @param question: string prompt to user
    @return: string lower case version of the recognised words
    """
    print(question)
    with microphone as source:
        audio = recognizer.listen(source)
    try:
        word_sr_return = recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        word_sr_return = "error: Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        word_sr_return = "error: Could not request results from Google Speech Recognition; {0}".format(e)
    print(word_sr_return)
    while "error" in word_sr_return:
        sad_tone()
        word_sr_return = get_sr(question)
    return word_sr_return

# start main
CodeePy.get_com_ports()
# Create a CodeePy instance so you can access its Class Methods
# You can use your robots name in lieu of board ie <Your Robots Name> = CodeePy('<Your COM Port>')
codee = CodeePy('COM12')
# Create a CodeeListen instance so you can access its Class Methods
recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.6 # 0.8 is default
microphone = sr.Microphone()

while True:
    command = get_sr("What would you like Codee to do?")

    if "arms" in command:
        if "swing" in command:
            codee.swing_arms(3)
        elif "up" in command:
            codee.set_arms(50,50)
        elif "down" in command:
            codee.set_arms(-50,-50)
        else:
            codee.stop_arms()
    elif "forward" in command:
        codee.set_wheel_velocities(10,10)
    elif "head" in command:
        if "look" in command:
            codee.look_around(3)
        else:
            codee.stop_head()
    elif "sing" in command:
        codee.set_melody_tempo(1)
        codee.play_melody("star wars")
    elif "happy" in command:
        codee.display_image("smile")
        codee.swing_arms(3)
    elif "sad" in command:
        codee.display_image("frown")
    elif "love" in command:
        codee.display_image("heart")
        codee.say("wooooottttwooooooooo")
    elif "stop" in command:
        codee.stop_arms()
        codee.stop_wheels()
        codee.stop_look_around()
    elif "exit" in command or "quit" in command or "end" in command:
        codee.reset_codee_body_and_exit()
        time.sleep(2)
        break
    else:
        codee.set_melody_tempo(3)
        sad_tone()



