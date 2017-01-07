# Implementation of classic arcade game Pong
# Graphical INterface at http://www.codeskulptor.org/

import simplegui
from random import randrange

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20.
PAD_WIDTH = 8.
PAD_HEIGHT = 80.
HALF_PAD_WIDTH = float(PAD_WIDTH / 2.)
HALF_PAD_HEIGHT = float(PAD_HEIGHT / 2.)
BALL_POS = [WIDTH/2., HEIGHT/2.]
BALL_VEL = ([randrange(2.,4.), randrange(1.,3.)])
LEFT = False
RIGHT = True
#paddle1_pos = ((HEIGHT/2.)-(HALF_PAD_HEIGHT))
#paddle2_pos = ((HEIGHT/2.)-(HALF_PAD_HEIGHT))
paddle1_vel = 0.
paddle2_vel = 0.

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global BALL_POS, BALL_VEL # these are vectors stored as lists
    BALL_POS = [WIDTH/2, HEIGHT/2]
    if direction:
        BALL_VEL = [(randrange(2,4)), -randrange(1,3)]
    else:
        BALL_VEL = [-(randrange(2,4)), -randrange(1,3)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global player1_score, player2_score  # these are ints
    player1_score = 0
    player2_score = 0
    paddle1_pos = ((HEIGHT/2.)-(HALF_PAD_HEIGHT))
    paddle2_pos = ((HEIGHT/2.)-(HALF_PAD_HEIGHT))
    spawn_ball(randrange(0,2))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel, player1_score, player2_score

        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if BALL_POS[1] <= BALL_RADIUS:
        BALL_VEL[1] = -BALL_VEL[1]
    if BALL_POS[1] >= HEIGHT-BALL_RADIUS:
        BALL_VEL[1] = -BALL_VEL[1]
    if BALL_POS[0] <= HALF_PAD_WIDTH+BALL_RADIUS and BALL_POS[1] > paddle1_pos and BALL_POS[1] < paddle1_pos+PAD_HEIGHT:
        BALL_VEL[0] = (-BALL_VEL[0])*1.25
        BALL_VEL[1] = (BALL_VEL[1])*1.25
    if BALL_POS[0] >= WIDTH-HALF_PAD_WIDTH-BALL_RADIUS and BALL_POS[1] > paddle2_pos and BALL_POS[1] < paddle2_pos+PAD_HEIGHT:
        BALL_VEL[0] = (-BALL_VEL[0])*1.25
        BALL_VEL[1] = (BALL_VEL[1])*1.25
    elif BALL_POS[0]<=BALL_RADIUS-(HALF_PAD_WIDTH/2):
        player2_score +=1
        spawn_ball(RIGHT)
    elif BALL_POS[0]>=WIDTH-BALL_RADIUS-(HALF_PAD_WIDTH/2):
        player1_score +=1
        spawn_ball(LEFT)
    
    BALL_POS[0] += BALL_VEL[0]
    BALL_POS[1] += BALL_VEL[1]      
    # draw ball
    canvas.draw_circle(BALL_POS, BALL_RADIUS, 2, "WHITE", "WHITE")
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= HEIGHT-PAD_HEIGHT:
        pass
    elif paddle2_pos + paddle2_vel >= HEIGHT-PAD_HEIGHT:
        pass
    elif paddle1_pos + paddle1_vel <= 0:
        pass
    elif paddle2_pos + paddle2_vel <= 0:
        pass
    else:
        paddle1_pos += paddle1_vel
        paddle2_pos += paddle2_vel
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos), (HALF_PAD_WIDTH/2, paddle1_pos), (HALF_PAD_WIDTH/2, (paddle1_pos+PAD_HEIGHT)), (0,((paddle1_pos)+PAD_HEIGHT))], 12, 'GRAY')
    canvas.draw_polygon([(WIDTH-(HALF_PAD_WIDTH/2), paddle2_pos), (WIDTH, paddle2_pos), (WIDTH, ((paddle2_pos)+PAD_HEIGHT)), ((WIDTH-HALF_PAD_WIDTH/2),((paddle2_pos)+PAD_HEIGHT))], 12, 'GRAY')
    # draw scores    
    canvas.draw_text(str(player1_score), [WIDTH/4, HEIGHT/5], 50, "White")    
    canvas.draw_text(str(player2_score), [WIDTH*3/4, HEIGHT/5], 50, "White")    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == 83:
        paddle1_vel += 3
    if key == 87:
        paddle1_vel -= 3
    if key == 40:
        paddle2_vel += 3
    if key == 38:
        paddle2_vel -= 3
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == 83 or key == 87:
       paddle1_vel = 0
    if key == 38 or key == 40:
        paddle2_vel = 0
def reset_handler():
    new_game()
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', reset_handler)

# start frame
new_game()
frame.start()
