import time
from codeepy import CodeePy

# view CodeePy Documentation
help(CodeePy)

CodeePy.get_com_ports()

# create CodeePy Instance and open connection (Change COM port to your own com port value)
# You can use your robots name in lieu of board ie <Your Robots Name> = CodeePy('<Your COM Port>')
board = CodeePy('COM12')

# say text
#board.say("Hello")

# set melody tempo
#board.set_melody_tempo(2)

# play melody
#board.play_melody("little lamb")

# play tone
#board.play_tone(2000, 300)

# play notes fixed duration
#board.play_notes(["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"], 1)  #C Major Scale
#board.exit()

#board.play_notes_with_duration(["C4.1", "D4.3", "E4.1", "F4.2", "G4.1", "A4.3", "B4.1", "C5.1"])
#board.exit()

#set left arm 30 degrees
#board.set_left_arm(30)

#Swing both arms for 5 seconds then stop
# set arms to on
#board.swing_arms(2, True)
# set delay
#time.sleep(5)
# stop arms
#board.stop_arms()
#board.exit()

#Set degrees of both arms
#board.set_arms(0, 0)

# test look around
# set look around to on
# board.look_around(2, True)
# set delay
#time.sleep(3)
# stop look around
#board.stop_look_around()

#Set head image
# board.display_image("tick")

#Text scroll
#board.led_scroll_text("abcde")

#Display number
#board.display_number(85)

#Clear Display
#board.display_clear()

#Set LED display pixel state
#board.set_led_display_pixel(0, 0, True)

#Changebluetooth name
#board.change_bot_bluetooth_name("Grumpee")

#Run single line sensor id no 5 for a maximum of 4 seconds
#board.read_line_sensor(5,4)

#returns an array of all the sensor values that detect a black line, 1 is true 0 is false
#You can all 5 or inner 3 sensors as int
#print(board.read_line_position(5))

#Test Codee's wheel servos
#for x in range(10):
#    board.set_left_wheel_velocity(10)
#    board.set_right_wheel_velocity(10)
#    time.sleep(0.25)
#board.set_left_wheel_velocity(0)
#board.set_right_wheel_velocity(0)

#Set both wheel speeds
#board.set_wheel_velocities(10,10)
#time.sleep(1)

#Reset Codee to default
board.reset_codee_body_and_exit()
