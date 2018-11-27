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
    pip install codeepy

    INSTRUCTIONS
    ============
    1. Insert your COM port (Line 42)
	3. Name your Codee instance, we have used board, you can call Codee what ever you like! (line 42) 

"""

import time
from codeepy import CodeePy

# view CodeePy Documentation
help(CodeePy)

CodeePy.get_com_ports()

# create CodeePy Instance and open connection
board = CodeePy('<Your COM port>')

# Dance intro loop
countdown = 5
for x in range(5): #Do every thing in this loop 5 times
    board.display_number(countdown) #Change the LED Matrix display to the number value of "countdown"
    countdown = countdown -1 #Take 1 from the number value of countdown
    board.set_left_arm(90) #Make left arm raised
    board.set_right_arm(90) #Make right arm raised
    board.play_tone(2000, 300) #A count down beep for each number
    time.sleep(1) #wait 1 second (while still doing all the above)

#Set scrolling display
board.led_scroll_text("DANCE") #Start text scroll on LED display matrix

#Start the music
board.play_melody("chariots") #Start playing the music

#Start arm swing
board.swing_arms(2) #Start swinging arms

#Spin from side to side
board.led_scroll_text("abc")

#Stop arm swing
board.stop_arms() #Stop swinging arms

#Start head dance
board.display_image("heart") #Change the LED Matrix display
board.look_around(2) #Make head move from side to side
time.sleep(8) #wait 5 seconds (while still doing all the above)

#Reset codee
board.reset_codee_body_and_exit()



