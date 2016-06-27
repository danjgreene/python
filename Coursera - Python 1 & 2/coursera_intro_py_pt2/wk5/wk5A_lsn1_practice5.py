# Ball grid solution

###################################################
# Student should enter code below

import simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw
def draw(canvas):
    iter = 1
    horiz = BALL_RADIUS * iter
    vert = BALL_RADIUS
    for ball in range(GRID_SIZE):
        canvas.draw_circle([horiz, vert], BALL_RADIUS, 1, 'White')
        iter += 1

                      
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()

