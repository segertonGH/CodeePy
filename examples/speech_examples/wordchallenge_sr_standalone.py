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

    GAME PLAY
    ==========
    1. Codee will choose a word from words.json
    2. Codee will then display the number of attempts given and the blank characters of the word
    3. User will then guess a letter by saying a word that begins with their chosen letter
    4. Codee will update the characters in the users guess and update the attempts left each turn
    5. Once there are no more attempts Codee will display a question mark
    6. User will guess word, if unsuccessful the answer will be displayed
    7. User will be asked if they want to continue playing

"""

import json
import random
import collections
import time
from codeepy import CodeePy
import speech_recognition as sr


def get_word():
    """
    This method returns a random word from the words.json file (must be in same package)
    """
    data = json.load(open('words.json'))
    wordlist = data['words']
    try:
        return random.choice(wordlist)
    except IndexError:
        print("nothing found")


def display_guess_list(remaining, g_list):
    """
    This method displays current guess list as string
    @param remaining: int remaining user attempts
    @param g_list: list of characters that represent the current user attempts
    """
    guess_text = ''.join(g_list)
    if remaining > 0:
        msg = str(remaining) + ":" + guess_text
    else:
        msg = "?" + guess_text
    board.led_scroll_text(msg)
    print(guess_text)


def correct():
    """
    This method makes codee respond a correct letter
    """
    board.display_clear()
    board.display_image("tick")
    board.swing_arms(4, True)
    time.sleep(3)
    board.stop_arms()
    board.display_clear()


def false():
    """
    This method makes codee respond an incorrect letter
    """
    board.display_clear()
    board.display_image("cross")
    board.set_arms(-90, -90)
    board.look_around(2, True)
    time.sleep(3)
    board.stop_look_around()
    board.display_clear()


def happy_tone():
    """
    This method makes codee play a happy sound
    """
    board.play_notes(["C5", "E5", "C5", "E5", "C5"], 1)
    time.sleep(1)


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


def get_letter_sr(question):
    """
    This method gets the first letter of speech recognition results
    @param question: string prompt to user
    @return: string lower case version of the recognised words first letter
    """
    letter_sr_return = get_sr(question)
    return letter_sr_return[0]


# start main
CodeePy.get_com_ports()
# Create a CodeePy instance so you can access its Class Methods
# You can use your robots name in lieu of board ie <Your Robots Name> = CodeePy('<Your COM Port>')
board = CodeePy('COM12')
board.set_melody_tempo(4)
recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.6 # 0.8 is default
microphone = sr.Microphone()

print("Lets play Word Challenge! \n" "Codee has a word in mind")

while True:
    # variables
    guess_list = []
    rand_word = get_word()  # get random word from jsonfile
    print(rand_word)
    counter = collections.Counter(rand_word)  # make counter object
    unique_chars_count = list(counter)  # count number of unique characters

    # calculate attempts
    attempts_remaining = len(unique_chars_count) - 1
    print("You have " + str(attempts_remaining) + " attempts")

    # create list of blank spaces (to be filled by users correct guesses)
    for x in rand_word:
        guess_list += "_"

    display_guess_list(attempts_remaining, guess_list)

    # loop while guessing letters
    while attempts_remaining > 0:
        # get user letter selection
        letter = get_letter_sr("Say a word that starts with your letter of choice")
        print("You said " + letter)

        occurrences = rand_word.count(letter)  # get occurrences of specified letter in word
        indices = [i for i, a in enumerate(rand_word) if a == letter]  # list of index's where the letter occurs
        board.display_clear()
        # add letter to guess_list if correct
        if len(indices) > 0:
            for x in indices:
                guess_list[x] = letter
            correct()
        else:
            false()
        attempts_remaining = attempts_remaining - 1  # set attempts
        display_guess_list(attempts_remaining, guess_list)  # display current guess status

    # finish challenge
    input_answer = get_sr("What do you think the word is?")

    if input_answer == rand_word:
        print("Yay you got it!")
        happy_tone()
        correct()
    else:
        print("Better luck next time!")
        sad_tone()
        false()
        board.display_clear()
        board.led_scroll_text("=" + rand_word)

    play_again = get_sr("Would you like to play again?")
    if play_again == "no" or play_again == "n":
        board.reset_codee_body_and_exit()
        break
