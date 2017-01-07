# implementation of card game - Memory
# Graphical Interface at http://www.codeskulptor.org/

import simplegui
import random
deck = range(8)+range(8)
exposed = [False]*len(deck)
d = {}
start = 0
end = 50
for i in range(0,len(deck)):
    d[i] = range(start,end)
    start+=50
    end+=50
state = 0
match = False
turns = 0    
# helper function to initialize globals
def new_game():
    global exposed, d, state, match, turns
    random.shuffle(deck)
    exposed = [False]*len(deck)
    print exposed
    d = {}
    start = 0
    end = 50
    for i in range(0,len(deck)):
        d[i] = range(start,end)
        start+=50
        end+=50
    print d
    print exposed
    print deck
    state = 0
    match = False
    turns = 0
# define event handlers
def mouseclick(pos):
    global d, exposed, match, turns, state, deck, first_card_v, first_card_k, second_card_v, second_card_k
    print pos
    for k,v in d.items():
        if pos[0] in v and exposed[k]:
            return
        else:
            pass
    if state == 0:
        print "start state is ", state
        for k,v, in d.items():
            if pos[0] in v:
                exposed[k] = True
                first_card_v = deck[k]
                first_card_k = k
                state = 1
                print first_card_v
        print "end state is ",state
    elif state == 1:
        print "start state is ", state
        for k,v in d.items():
            if pos[0] in v and not exposed[k]:
                exposed[k] = True
                second_card_v = deck[k]
                second_card_k = k
                print second_card_v
                if first_card_v == second_card_v:
                    match = True
                state = 2
        print "end state is ", state
        turns+=1
    else:
        print "start state is ", state
        if not match:
            exposed[first_card_k] = False
            exposed[second_card_k]= False
        for k,v in d.items():
            if pos[0] in v and not exposed[k]:
                exposed[k] = True
                first_card_v = deck[k]
                first_card_k = k
                print "first card of next turn is: ",first_card_v
        match = False
        state = 1
        print "end state is ", state
    print "Turns =", turns
# cards are logically 50x100 pixels in size    
def draw(canvas):
    n = 0
    for k in range(len(deck)):
        x = (800/16) * n
        if exposed[k]:
            canvas.draw_text(str(deck[k]), [x+18, 62], 24, "White")
        else:
            canvas.draw_polygon([[x, 0],[x+50,0],[x+50,100],[x,100]], 2, "Black", "Green")
        n += 1
    label.set_text("Turns = "+str(turns))
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric