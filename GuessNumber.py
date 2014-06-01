
import random
import math
import simplegui

secret_num=0
guess=0
count=0
total_guess=0


def new_game(low,high):
    global secret_num, total_guess, count
    if (high==100):        
        secret_num= random.randrange(0,100)
        total_guess= int(math.log(100-0+1)/math.log(2))+1
        print "New Game. range 0 to 100 "
        print "Number of remaining guesses is", total_guess
        count=0
    elif (high==1000):
         secret_num= random.randrange(0,1000)
         total_guess=int(math.log(1000-0+1)/math.log(2))+1
         print "New Game. range 0 to 1000"
         print "Number of remaining guesses is", total_guess
         count=0

# define event handlers for control panel
def range100():     
    new_game(0, 100)
      
def range1000():
   new_game(0, 1000)

def input_guess(guess):
    global count
    count=count+1
    
    guess_me= int(guess)
    print " "
  
    if count<total_guess:
        if secret_num > guess_me:
            print "Guess was", guess_me
            remaining_count = total_guess-count
            print "Number of remaning Guess is", remaining_count
            print "Higher!"
            print " "
            
        elif secret_num < guess_me: 
            print "Guess was", guess_me
            remaining_count = total_guess-count
            print "Number of remaning Guess is", remaining_count 
            print "Lower!"
            print" "
            
        elif secret_num == guess_me:
            print "Guess was", guess_me
            remaining_count = total_guess-count
            print "Number of remaning Guess is", remaining_count 
            print "Correct!"
            print " "
            new_game(0,100)
            print" "         
            
    else: 
        print "Guess was", guess_me
        print "Number of remaining guess is", 0
        print "You ran out of guess. The number was:", secret_num
        print" "
        new_game(0,100)
        print" "
   
print " " 


# create frame

f= simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements

f.add_button("Range is [0,100)", range100,200)
f.add_button("Range is [0, 1000)", range1000,200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game and start frame

f.start()
new_game(0,100)

