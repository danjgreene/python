# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, 0] # pixels per update (1/60 seconds)

paddle1_pos = HEIGHT / 2 # vertical pos component; horizontal pos is constant(see handler)
paddle2_pos = HEIGHT / 2 # vertical pos component; horizontal pos is constant(see handler)

paddle1_vel = 0 # vertical pixels per update (1/60 seconds)
paddle2_vel = 0 # vertical pixels per update (1/60 seconds)

score1 = 0
score2 = 0


# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
   
    if direction == RIGHT: 
        ball_vel = [random.randrange(2, 4), -(random.randrange(1, 3))]
    elif direction == LEFT: 
        ball_vel = [-(random.randrange(2, 4)), -(random.randrange(1, 3))] 

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
   
    # collide and reflect off of top of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]    
    # collide and reflect off of top of canvas
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
   
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
   
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos+ paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
        
    # draw paddle1
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # draw paddle2
    canvas.draw_line([(WIDTH - HALF_PAD_WIDTH), paddle2_pos - HALF_PAD_HEIGHT],[(WIDTH - HALF_PAD_WIDTH), paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide -- or if ball collides with gutters
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and (paddle1_pos + HALF_PAD_HEIGHT >= ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT):
        ball_vel[0] = (- ball_vel[0]) * 1.1 # left paddle collision -- increase velocity by 10%
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS and (paddle2_pos + HALF_PAD_HEIGHT >= ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT):
        ball_vel[0] = (- ball_vel[0]) * 1.1 # right paddle collision -- increase velocity by 10%
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:  
        spawn_ball(RIGHT) # left gutter collision
        score2 += 1 # paddle2 player gets a point
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:  
        spawn_ball(LEFT) # right gutter collision
        score1 += 1 # paddle1 player gets a point
    
    # draw scores
    canvas.draw_text(str(score1), (150, 60), 32, 'Yellow', 'sans-serif')
    canvas.draw_text(str(score2), (450, 60), 32, 'Yellow', 'sans-serif')
        
def keydown(key):
    
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -4
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 4
   
def keyup(key):
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# restart button
def button():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart_button = frame.add_button('Restart', button)


# start frame
new_game()
frame.start()
