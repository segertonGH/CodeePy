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
codee = CodeePy('COM12')

# Dance intro loop
countdown = 5
for x in range(5): #Do every thing in this loop 5 times
    codee.display_number(countdown) #Change the LED Matrix display to the number value of "countdown"
    countdown = countdown -1 #Take 1 from the number value of countdown
    codee.set_left_arm(50) #Make left arm raised
    codee.set_right_arm(50) #Make right arm raised
    codee.play_tone(2000, 300) #A count down beep for each number
    time.sleep(1) #wait 1 second (while still doing all the above)

#Set scrolling display
codee.led_scroll_text("DANCE") #Start text scroll on LED display matrix

#Start the music
codee.play_melody("chariots") #Start playing the music

#Start arm swing
codee.swing_arms(2) #Start swinging arms

#Start head dance
codee.look_around(2) #Make head move from side to side
time.sleep(20) # wait 20 seconds (while still doing all the above)

#Stop arm swing
codee.stop_arms() #Stop swinging arms

#Reset codee
codee.reset_codee_body_and_exit()



