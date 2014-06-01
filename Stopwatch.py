import simplegui
import math

# define global variables

tick=0
total_stop=0
correct_stop=0
score=0

# define helper function that converts time
def time_converter(time):
    
    minute= int(time/600)
    remain= time-(minute*60*10)
    tens_sec= int(remain)/100
    sec= ((remain/10)%10)
    tenth_sec=(remain%10)
    return str(minute)+":"+ str(tens_sec)+str(sec) + "." + str(tenth_sec)    

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global tick
    increment()
    tick_timer.start()    

def increment():
    global tick
    tick+=1

def stop():
    global total_stop, correct_stop
    
    if tick_timer.is_running() ==True:
        tick_timer.stop()
        
        if (tick%10 ==0):
           total_stop+=1
           correct_stop+=1
           
        else:
            total_stop+=1
            correct_stop=correct_stop

def score_game(score):
    return str(correct_stop)+"/"+str(total_stop)
    
def reset():
    global tick, total_stop, correct_stop
    tick=0
    total_stop=0
    correct_stop=0

# define event handler for timer with 0.1 sec interval
tick_timer=simplegui.create_timer(100, start)

# define draw handler
def draw (canvas):
    canvas.draw_text(time_converter(tick), [120,160], 45, "Red")
    canvas.draw_text(score_game(score),[220,50], 30, "white")
                     
# create frame
frame=simplegui.create_frame("StopWatch:The game",300,300)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset",reset,100)
frame.set_draw_handler(draw)

# start frame
frame.start()
