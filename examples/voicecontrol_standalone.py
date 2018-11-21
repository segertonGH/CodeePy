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

"""

import time
from codeepy import CodeePy
import speech_recognition as sr


def sad_tone():
    """
    This method makes codee play a sad sound
    """
    board.play_notes_with_duration(["F4.1", "B3.1"])


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
board = CodeePy('COM12')
# Create a CodeeListen instance so you can access its Class Methods
recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.6 # 0.8 is default
microphone = sr.Microphone()

while True:
    command = get_sr("What would you like Codee to do?")

    if "arms" in command:
        if "swing" in command:
            board.swing_arms(3, True)
        elif "up" in command:
            board.set_arms(90,90)
        elif "down" in command:
            board.set_arms(-90,-90)
        else:
            board.stop_arms()
    elif "forward" in command:
        board.set_wheel_velocities(10,10)
    elif "head" in command:
        if "look" in command:
            board.look_around(3,True)
        else:
            board.stop_look_around()
    elif "sing" in command:
        board.play_melody("star wars")
    elif "happy" in command:
        board.display_image("smile")
        board.swing_arms(3,True)
    elif "sad" in command:
        board.display_image("frown")
    elif "love" in command:
        board.display_image("heart")
        board.say("wooooottttwooooooooo")
    elif "stop" in command:
        board.stop_arms()
        board.stop_wheels()
        board.stop_look_around()
    elif "exit" in command or "quit" in command or "end" in command:
        board.reset_codee_body_and_exit()
        time.sleep(2)
        break
    else:
        board.set_melody_tempo(3)
        sad_tone()



