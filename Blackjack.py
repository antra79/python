Blackjack.py
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")   

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
player_hand_value=0
dealer_hand_value=0
player_hand=()
dealer_hand=()
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
   
    
# define hand class
class Hand:
    def __init__(self): # create Hand object
        self.hand=[]      

    def __str__(self):
        s="Hand Contains "
        for i in self.hand:
            s+=i.get_suit()+ i.get_rank()+ " "
        return s
   
    def add_card(self,card):
        self.hand.append(card)       

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
       
        hand_value=0
        for i in self.hand:
            if (i.get_rank() =='A' and hand_value<=10):
                hand_value+=11
            else:
                hand_value+=VALUES[i.get_rank()]
        return hand_value
       
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        temp_pos=pos[:]
        for card in self.hand:
            card.draw(canvas,temp_pos)
            temp_pos[0]+=100
        if in_play==True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [135,350], CARD_BACK_SIZE)
    
         
# define deck class
class Deck:
    def __init__(self): # create a Deck object
        self.deck=[]
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i,j))
        
    def __str__(self): # return a string representing the deck
        s="Deck Contains:"
        for i in self.deck:
            s+=(i.get_suit()+i.get_rank())+" "
        return s
     
    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck)    # use random.shuffle()
       
    def deal_card(self): # deal a card object from the deck
        return self.deck.pop()   
   

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand
    global player_hand_value, dealer_hand_value, score
   
    deck = Deck()
    deck.shuffle()
   
    player_hand=Hand()
    dealer_hand=Hand()
   
    for i in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
       
    print "Player " + str(player_hand)
    print "Dealer " + str(dealer_hand)
   
    player_hand_value= player_hand.get_value()
    dealer_hand_value=dealer_hand.get_value()
   
    print player_hand_value
    print dealer_hand_value
   
    if in_play:
        outcome = "Game interrupted, player lost! New Game?"
        score-=1
    else:
        outcome="Hit or Stand?"   
   
    in_play = True

def hit():
    global outcome, in_play, player_hand_value,dealer_hand_value
    global player_hand, dealer_hand, score
   
    deck=Deck()
   
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(deck.deal_card())
        player_hand_value= player_hand.get_value()
        print "Player " + str(player_hand)
        print player_hand_value
   
        # if busted, assign a message to outcome, update in_play and score
        if player_hand_value >21:
            outcome = "Player busted! New Game?"
            in_play=False
            score-=1
           
      
def stand():  
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global player_hand_value, dealer_hand_value, dealer_hand
    global outcome, in_play, score
   
    print dealer_hand_value
   
    deck=Deck()
    if not in_play:return
   
    if player_hand_value>21:
        outcome= "Player busted! New Game?"
        score-=1
    else:
        while dealer_hand_value <17:
            dealer_hand.add_card(deck.deal_card())
            dealer_hand_value=dealer_hand.get_value()
            print "Dealer " + str(dealer_hand)
            print "dealer_hand_value " + str(dealer_hand_value)
        if dealer_hand_value >21:
            outcome = "Dealer busted! New Game?"
            score+=1
        else:
            if player_hand_value > dealer_hand_value:
                outcome = "Player won!"
                score+=1
            else:
                outcome = "Player lost!"
                score-=1
 
    # assign a message to outcome, update in_play and score
    in_play = False
   

# draw handler   
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
   
    card1 =Card("D", "A")
    card2=Card("S","3")
   
    canvas.draw_text("BLACKJACK",[200,75], 35, "BLACK")
    canvas.draw_text("DEALER",[100,250], 25, "BLACK")
    canvas.draw_text("PLAYER",[100,450], 25, "BLACK")
    canvas.draw_text(outcome, [300, 450], 15, "WHITE")
    canvas.draw_text('Score = '+str(score), (200, 150), 24, "White")
   
    pos=[100,300]
    dealer_hand.draw(canvas,pos)
    player_hand.draw(canvas,[pos[0],pos[1]+180])
   

# initialization frame
frame = simplegui.create_frame("Blackjack", 700, 700)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric