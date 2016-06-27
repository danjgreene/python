# Echo mouse click in console

###################################################
# Student should enter code below

# Examples of mouse input

import simplegui
import math

# intialize globals
WIDTH = 450
HEIGHT = 300

# define event handler for mouse click, draw
def click(pos):
    print "Mouse click at " + str(pos)

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)


# start frame
frame.start()
    



###################################################
# Sample output

#Mouse click at (104, 105)
#Mouse click at (169, 175)
#Mouse click at (197, 135)
#Mouse click at (176, 111)
#Mouse click at (121, 101)
#Mouse click at (166, 208)
#Mouse click at (257, 235)
#Mouse click at (255, 235)