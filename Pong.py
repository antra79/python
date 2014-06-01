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
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0,0]
paddle1_pos=[HALF_PAD_WIDTH-1, HEIGHT/2]
paddle2_pos=[WIDTH+1-HALF_PAD_WIDTH, HEIGHT/2]
paddle1_vel=0
paddle2_vel=0
player1_score=0
player2_score=0
paddle1_top=paddle1_pos[1]-HALF_PAD_WIDTH
paddle1_bottom=paddle1_pos[1]+HALF_PAD_WIDTH
paddle2_top=paddle2_pos[1]-HALF_PAD_WIDTH
paddle2_bottom=paddle2_pos[1]+HALF_PAD_WIDTH
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(RIGHT):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH/2, HEIGHT/2]
    ball_vel[0]=random.randrange(2,4)
    ball_vel[1]=random.randrange(1,3)

    if RIGHT== False:
        ball_vel[0]=-ball_vel[0]  
    #ball_vel[1]=-ball_vel[1]
    
#define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,player1_score,player2_score
    paddle1_pos=[HALF_PAD_WIDTH-1, HEIGHT/2]
    paddle2_pos=[WIDTH+1-HALF_PAD_WIDTH, HEIGHT/2]
    player1_score=0
    player2_score=0
    if random.randrange(0,2) == 0:
        spawn_ball(True)
    else:
        spawn_ball(False)
    
def draw(canvas):
    global paddle1_vel, paddle2_vel, player1_score, player2_score
    global paddle1_pos, paddle2_pos,paddle_top, paddle_bottom

   # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    
    ball_pos[0]+=int(ball_vel[0])
    ball_pos[1]+=int(ball_vel[1])
    
    #ball collision with top and bottom walls
    if (int(ball_pos[1])>= HEIGHT-BALL_RADIUS): #collision with bottom wall  
       ball_vel[1]= -ball_vel[1]
   
    elif int(ball_pos[1])<= BALL_RADIUS: #collision with top wall
        ball_vel[1]=-ball_vel[1]
    
    # ball colision with left gutters and left paddles
    
   
    if (int(ball_pos[0])<= (BALL_RADIUS + PAD_WIDTH)) and (paddle1_bottom< int(ball_pos[1]) <paddle1_top):        
        ball_vel[0]= -ball_vel[0]
        ball_vel[0]*=1.1
        ball_vel[1]*=1.1
        
          
    elif int(ball_pos[0])<= (BALL_RADIUS +PAD_WIDTH):  
        ball_vel[0]= -ball_vel[0]
        player2_score+=1
        spawn_ball(True)
   
   # ball colision with right gutters and rigth paddles
        
    if (int(ball_pos[0])>= (WIDTH+1-BALL_RADIUS-PAD_WIDTH)) and (paddle2_bottom<int(ball_pos[1])<paddle2_top):  #and (int(ball_pos[1]) in range(paddle2_pos[1]+HALF_PAD_WIDTH, paddle2_pos[1]-HALF_PAD_WIDTH):
        ball_vel[0]= -ball_vel[0]
        ball_vel[0]*=1.1  #10% increase in ball velocity
        ball_vel[1]*=1.1        
        
    elif int(ball_pos[0])>=(WIDTH+1-BALL_RADIUS): 
        ball_vel[0]= -ball_vel[0]
        player1_score+=1
        spawn_ball(False)
               
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "Red")

   # update paddle's vertical position, keep paddle on the screen
   
    if (paddle1_pos[1]>HALF_PAD_HEIGHT) and (paddle1_pos[1]< HEIGHT-HALF_PAD_HEIGHT):
        paddle1_pos[1]+=paddle1_vel
    elif (paddle1_pos[1]==HALF_PAD_HEIGHT) and paddle1_vel>0:
         paddle1_pos[1]+=paddle1_vel
    elif (paddle1_pos[1]==HEIGHT-HALF_PAD_HEIGHT) and (paddle1_vel<0):
        paddle1_pos[1]+=paddle1_vel
 
    if (paddle2_pos[1]>HALF_PAD_HEIGHT) and (paddle2_pos[1]< HEIGHT-HALF_PAD_HEIGHT):
        paddle2_pos[1]+=paddle2_vel
    elif (paddle2_pos[1]==HALF_PAD_HEIGHT) and paddle2_vel>0:
         paddle2_pos[1]+=paddle2_vel
    elif (paddle2_pos[1]==HEIGHT-HALF_PAD_HEIGHT) and (paddle2_vel<0):
        paddle2_pos[1]+=paddle2_vel
    
    
    # draw paddles
    canvas.draw_polygon([[paddle1_pos[0]-HALF_PAD_WIDTH,paddle1_pos[1]+HALF_PAD_HEIGHT],
                         [paddle1_pos[0]+HALF_PAD_WIDTH,paddle1_pos[1]+HALF_PAD_HEIGHT],
                         [paddle1_pos[0]+HALF_PAD_WIDTH,paddle1_pos[1]-HALF_PAD_HEIGHT],
                         [paddle1_pos[0]-HALF_PAD_WIDTH,paddle1_pos[1]-HALF_PAD_HEIGHT]],8,"Green")
    
    canvas.draw_polygon([[paddle2_pos[0]-HALF_PAD_WIDTH,paddle2_pos[1]+HALF_PAD_HEIGHT],
                         [paddle2_pos[0]+HALF_PAD_WIDTH,paddle2_pos[1]+HALF_PAD_HEIGHT],
                         [paddle2_pos[0]+HALF_PAD_WIDTH,paddle2_pos[1]-HALF_PAD_HEIGHT],
                         [paddle2_pos[0]-HALF_PAD_WIDTH,paddle2_pos[1]-HALF_PAD_HEIGHT]],8,"Green")
    # draw scores
    canvas.draw_text(str(player1_score), [50,50],30,"Red")
    canvas.draw_text(str(player2_score), [400,50],30,"Red")
  
  
  
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['s']:
        paddle1_vel=4

    elif key==simplegui.KEY_MAP['down']:
        paddle2_vel=4       
        
def keyup(key):
    global paddle1_vel, paddle2_vel
 
    if key==simplegui.KEY_MAP['w']:
        paddle1_vel=-4

    elif key==simplegui.KEY_MAP['up']:
        paddle2_vel=-4

def restart():
    global ball_pos, paddle1_pos, paddle2_pos, player1_score
    global player2_score
    ball_pos=[WIDTH/2, HEIGHT/2]
    paddle1_pos=[HALF_PAD_WIDTH-1, HEIGHT/2]
    paddle2_pos=[WIDTH+1-HALF_PAD_WIDTH, HEIGHT/2]
    spawn_ball(RIGHT)
    player1_score=0
    player2_score=0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart)


# start frame
new_game()
frame.start()
