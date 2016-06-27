# implementation of card game - Memory

import simplegui
import random

#static variables
FRAME_WIDTH = 800
FRAME_HEIGHT = 100
turns = 0

# helper function to initialize globals
def new_game():
    
    global exposed
    global crd_state
    global first_crd
    global sec_crd
    global card_index
    global prev_crd1_idx
    global prev_crd2_idx
    global turns
    global cards
    global cards2
    global exposed
    
    # tracking card flip state
    card_index = 0
    #turns = 0
    crd_state = 0
    first_crd = int()
    sec_crd = int()
    prev_crd1_idx = int()
    prev_crd2_idx = int()
    
    # shuffled card deck
    cards = range(0,8)
    cards2 = range(0,8)
    exposed = [False] * 16 
    cards.extend(cards2) #Now we have combined lists
    random.shuffle(cards)
    
    #turns = 0

  

# counter to keep track of turns
def counter():
    global turns
    turns += 1
     
# define event handlers (NOTE: cards[card_index] is the number on the card)
def mouseclick(pos):
    global exposed
    global crd_state
    global first_crd
    global sec_crd
    global card_index
    global prev_crd1_idx
    global prev_crd2_idx
    global turns
    
    card_index = pos[0] // 50
    print
    print "card index = " + str(card_index)
    if exposed[card_index] == False:
        exposed[card_index] = True
        
        if crd_state == 0:
            crd_state = 1
            print "card state = " + str(crd_state)
            first_crd = cards[card_index]
            prev_crd1_idx = card_index
            print "1st card = " + str(first_crd)
            
        elif crd_state == 1:
            crd_state = 2
            print "card state = " + str(crd_state)
            sec_crd = cards[card_index]
            prev_crd2_idx = card_index
            print "2nd card = " + str(sec_crd)

        else: #(card_state == 2)
            crd_state = 1
            print "card state = " + str(crd_state)
            
            if first_crd != sec_crd:
                exposed[prev_crd1_idx] = False
                exposed[prev_crd2_idx] = False
                prev_crd1_idx = int()
                prev_crd2_idx = int()
                first_crd = int()
                sec_crd = int()

            first_crd = cards[card_index]
            prev_crd1_idx = card_index
            print "1st card = " + str(first_crd)
            counter()
            print "turns = " + str(turns)
            label.set_text("Turns = " + str(turns))
            
           

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card_index
    global card_pos
    global crd_cvr_pos
    for card_index in range(len(cards)):
        card_pos = [50 * card_index + 12.5, FRAME_HEIGHT / 2 + 12.5]
        crd_cvr_pos = [(50 * card_index, 0), (50 * card_index, 100), 
                       (50 + (50 * card_index), 100), (50 + (50 * card_index), 0)]
        canvas.draw_text(str(cards[card_index]), card_pos, 40, 'Gray', 'sans-serif')
        if exposed[card_index] == False:
            canvas.draw_polygon(crd_cvr_pos, 1, 'Black', 'Green')
    
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", FRAME_WIDTH, FRAME_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric