# implementation of card game - Memory
import simplegui
import math
import random

Height=100
Width=50
deck = range(0,8)*2
deck1 = random.shuffle(deck)
exposed=[False]*16
game_state=0
firstclick_cardNum=0
secondclick_cardNum=0
cardNum=0
cardNum1=0
cardNum2=0
turn=0

# helper function to initialize globals
def new_game():
    global exposed,game_state, turn,cardNum,cardNum1,cardNum2
    exposed=[False]*16
    game_state=0
    turn=0
    cardNum=0
    cardNum1=0
    cardNum2=0

def checkcardNumOnClick(x):
    counter=-1
    for i in range(0,800,50):
        if (x<i+1):
            break
        else:
            counter=counter+1
            continue                
    return counter       

def move(x):
    exposed[x]=True
    return exposed    

def turn_click():
    global turn
    turn+=1

 # define event handlers   
def mouse_handler(pos):
    global game_state, card_pos, firstclick_cardNum, cardNum1
    global secondclick_cardNum, cardNum2,cardNum,turn
    turn_click()
    if game_state==0:       
        cardNum1=checkcardNumOnClick(pos[0])
        firstclick_cardNum=deck[cardNum1]        
        move(cardNum1)
        game_state=1        
    
    elif game_state==1:        
        cardNum2=checkcardNumOnClick(pos[0])
        secondclick_cardNum=deck[cardNum2]        
        move(cardNum2)                
        game_state=2
        
    else:
        if firstclick_cardNum == secondclick_cardNum:
            exposed[cardNum1]=True
            exposed[cardNum2]=True
            cardNum=checkcardNumOnClick(pos[0])
            move(cardNum)
            cardNum1 = cardNum
            firstclick_cardNum=deck[cardNum1]
            game_state=1
            
        else:
            exposed[cardNum1]=False
            exposed[cardNum2]=False
            cardNum=checkcardNumOnClick(pos[0])
            move(cardNum)
            cardNum1 = cardNum
            firstclick_cardNum=deck[cardNum1]
            game_state=1

 # cards are logically 50x100 pixels in size           
def draw(canvas):
    game_state=1
    for i in range (16):
        if exposed[i]== True:
            canvas.draw_text(str(deck[i]), (20+i*Width,60), 25, "Red")
        else:     
            canvas.draw_line((25+i*Width,0),(25+i*50,Height),48,"green")  
    label.set_text("Turn="+str(turn)) 
# create frame and add a button and labels   
frame=simplegui.create_frame("Test", 800,100)
frame.set_draw_handler(draw)
# register event handlers
frame.set_mouseclick_handler(mouse_handler)
frame.add_button("Restart",new_game)
label=frame.add_label("Turn=0")

# get things rolling
frame.start()
new_game()