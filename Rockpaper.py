import random
def name_to_number(name):
    ''' This  function converts the name (player' choice) 
    to a number'''
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name =="lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Entered name is not a valid name"

def number_to_name(number):
    '''This function converts a number to a name'''  
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number ==4:
        return "scissors"
    else:
        return "The number is not in the correct range" 
    
def rpsls(player_choice): 
    ''' This function genrates a random number and assign it 
    as computer's choice and compare it to the player_choice 
    and decides the winner
    '''
    print " "
    print "Player chooses", player_choice
    
    player_number = name_to_number(player_choice)
    random_guess = random.randrange(0,5)
    computer_number=random_guess
    comp_choice = number_to_name(random_guess)
    print "Computer chooses", comp_choice
    diff = (computer_number - player_number) % 5
    
    if (diff == 1) or (diff == 2):
        print "Player Wins!"
    elif (diff==3) or (diff== 4):
        print "Computer Wins!"
    else:
        print "Player and Computer have a tie"
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


