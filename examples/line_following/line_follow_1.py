"""
LICENSE:
===============

    Copyright (c) 2023 Simon Egerton and the Creative Science Foundation. All rights reserved.

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

    NOTES:
    ===============
    
    This example demostrates a basic line following algrothim, based on a 
    Braitenberg statemachine.  This example assumes a black line on a white background. Ideally 
    the line should be about 15mm wide, or roughly the half the distance between two sensors.  
    Codee uses the readline() function to update the lineState class variable.  
    lineState is an integer value between 0 and 10 with the following meaning when 5 line sensors 
    are installed.

     0 Codee the the very, very, very, left of line
     1 Codee the the very, very, left of line
     2 Codee the the very, left of line
     3 Codee the the left of line
     4 Codee on line centre
     5 Codee the the right of line
     6 Codee the the very, right of line
     7 Codee the the very, very, right of line
     8 Codee the the very, very, very, right of line
     9 All sensors are not reflecting i.e. all sensors on the line
     10 All sensors are reflecting, i.e. all sensor off the line, on reflective area   
 
     lineSate is used to index an array of wheel velocities.  This allows for the implementation of 
     a range of line following behaviours and the use of machine and reinforcement learning to 
     enable Codee to learn how to optimally follow a line.
 
     In this example the state array has been filled with a set of left / right wheel 
     velocities to effect a simple line following behaviour.  You may need to tweak them 
     to suit your Codee.

    INSTRUCTIONS
    ============
    1. Insert your COM port at line 75
    2. Run the program and codee will follow a black line on a white background
    3. To exit press "CTRL-C" to exit

    NOTES
    =====
"""

from codeepy import *

# state array maps to -> [VVVL, VVL, VL, L, CENTRE, R, VR, VVR, VVVR, ALL ON, ALL OFF]
# line following states
lf_state_leftw =    [ 10, 10, 10, 10, 10, 3, 3,	3,	3,	0,	0 ];
lf_state_rightw =   [ 3, 3,	3,	3,	10,	10,	10,	10,	10,	0,	0 ];

# display list of COM ports
CodeePy.get_com_ports()

# create CodeePy Instance and open connection
codee = CodeePy('COM8')

# follow line until CTRL-C is pressed
try:
    print("Line follower STARTED")
    while (True):
        # read line position and state, this example only uses the state
        line_position, line_state = codee.read_line_sensors_position_and_state(5)
    
        # update codees velocity state
        codee.set_wheel_velocities(lf_state_leftw[line_state], lf_state_rightw[line_state])
except KeyboardInterrupt:
    print("Line follower STOPED")
    codee.stop_wheels()