# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

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
    def __init__(self):
        self.hand = [] # initialize Hand object empty list

    def __str__(self):
        # return a string representation of a hand
        self.hand_str = ""
        for i in range(len(self.hand)):
            self.hand_str += str(self.hand[i]) + " "
        return "Hand contains " + self.hand_str
        
    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        
        self.value = 0
        has_aces = False
        for crd in self.hand:
            self.value += VALUES.get(crd.get_rank())
            if crd.get_rank() == 'A':
                has_aces = True
        if has_aces == True:
            if self.value + 10 <= 21:
                return self.value + 10
            else:
                return self.value
        return self.value
   
    def draw(self, canvas, pos):
        tick = 0
        for cd in self.hand:
            cd.draw(canvas, [pos[0] + (tick * (pos[0] + 20)), pos[1]])
            tick += 1
  
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS: 
            for rank in RANKS:
        # create a Card object using Card(suit, rank) and add it to the card list for the deck  
                card = Card(suit, rank)
                self.deck.append(card)
        return self.deck
            
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):     
        return self.deck.pop(0)
       
    def __str__(self):
        self.deck_str = ""
        for c in range(len(self.deck)):
            self.deck_str += str(self.deck[c]) + " "
        return "Deck contains " + self.deck_str


#define event handlers for buttons
def deal():
    global outcome, in_play, my_deck, my_hand, dealer_hand, score
    my_deck = Deck()
    my_hand = Hand()
    dealer_hand = Hand()
    
    my_deck.shuffle()
    my_hand.add_card(my_deck.deal_card())
    #my_hand.draw(canvas, pos)
    my_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    
    in_play = True
    
    print "Player: " + str(my_hand)
    print "Dealer: " + str(dealer_hand)
    
    outcome = "Hit or stand?"

def hit():
    global outcome, in_play, my_deck, my_hand, dealer_hand, score
    
    if my_hand.get_value() <= 21: #in_play = True
        my_hand.add_card(my_deck.deal_card())
        print "Player: " + str(my_hand)
        if my_hand.get_value() <= 21:
            in_play = True
        else:
            in_play = False
            print "You have busted"
            print "Dealer wins"
            outcome = "Dealer wins"
            score -= 1
    else:
        print "You have busted"
        print "Dealer wins"
        outcome = "You have busted -- Dealer wins"
        score -= 1
    
def stand():
    global outcome, in_play, my_deck, my_hand, dealer_hand, score
    
    in_play = False
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if my_hand.get_value() <= 21: #in_play = True
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(my_deck.deal_card())
        if dealer_hand.get_value() == 21:
            print "Dealer: " + str(dealer_hand)
            print "Dealer wins"
            outcome = "Dealer wins"
            score -= 1
        if 21 > dealer_hand.get_value() > my_hand.get_value():
            print "Dealer: " + str(dealer_hand)
            print "Dealer wins"
            outcome = "Dealer wins"
            score -= 1
        else:
            print "Dealer: " + str(dealer_hand)
            print "Player wins"
            outcome = "Player wins"
            score += 1
    else:
        print "You have busted -- Dealer wins"
        outcome = "You have busted -- Dealer wins"
        score -= 1
            
# draw handler    
def draw(canvas):
    
    if in_play:
        dealer_hand.draw(canvas, [72, 200])
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [108,248], CARD_SIZE)
    else:
        dealer_hand.draw(canvas, [72, 200])
        
    my_hand.draw(canvas, [72, 400])

    canvas.draw_text('Blackjack', (72, 72), 44, 'Black')
    canvas.draw_text("Score: " + str(score), (275, 72), 28, 'White', 'sans-serif')
    canvas.draw_text('Dealer', (72, 175), 28, 'Black', 'sans-serif')
    canvas.draw_text('Player', (72, 375), 28, 'Black', 'sans-serif')
    canvas.draw_text(outcome, (275, 375), 28, 'White', 'sans-serif')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
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