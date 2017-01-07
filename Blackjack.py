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
game_over = False
outcome = "Hit or Stand?"
score = 0
game_deck = []
player = []
dealer = []
Score = 0

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
        self.hand_cards = []

    def __str__(self):
        now_holding = ""
        for i in range(len(self.hand_cards)):
            now_holding += str(self.hand_cards[i])
            now_holding += " "
        return "hand contains " + str(now_holding)

    def add_card(self, card):
        self.get_new_card = self.hand_cards.append(card)

    def get_value(self):
        self.hand_value = 0
        for each in self.hand_cards:
            for r in RANKS:
                for s in SUITS:
                    test = s+r
                    if test == str(each):
                        self.hand_value+=VALUES[r]            
        for each in self.hand_cards:
            if "A" not in str(each):
                pass
            else:
                if self.hand_value+10 <= 21:
                    self.hand_value+=10
                else:
                    return self.hand_value
        return self.hand_value
    def draw(self, canvas, pos):
#        print pos #alter the pos[0] and pos[1] variables to displace n times the number of cards
        n = 0
        for each in self.hand_cards:
            n+=1
            r = str(each)[1]
            s = str(each)[0]
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(r), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(s))
#            if n == 1:
#                print n, self.hand_cards,each
#                canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0]*n + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            if n == 1 and (each in dealer.hand_cards):
                print each
                card_loc = (CARD_CENTER[0]+CARD_SIZE[0], 
                    CARD_CENTER[1])
                canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)    
            else:
                canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0]*n + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            
            # draw a hand on the canvas, use the draw method for cards

   
        
# define deck class 
class Deck:
    def __init__(self):
        self.card_deck = []
        for s in SUITS:
            for r in RANKS:
                self.card_deck.append(Card(s,r))
    def shuffle(self):
        random.shuffle(self.card_deck)

    def deal_card(self):
        return self.card_deck.pop()
    
    def __str__(self):
        new_deck = ""
        for j in range(len(self.card_deck)):
            new_deck+= str(self.card_deck[j])
            new_deck+=" "
        return "Deck contains " + new_deck     


#define event handlers for buttons
def deal():
    global outcome, in_play, game_deck, player, dealer, Score, game_over
    if in_play and not game_over:
        Score -=1
    in_play = True
    game_over = False
    game_deck = Deck()
    game_deck.shuffle()
    print game_deck
    player = Hand()
    player.add_card(game_deck.deal_card())
    player.add_card(game_deck.deal_card())
    dealer = Hand()
    dealer.add_card(game_deck.deal_card())
    dealer.add_card(game_deck.deal_card())
    print game_deck
    print "player's " + str(player)
    print "dealer's " + str(dealer)
    print "player hand value is " +str(player.get_value())
    print "dealer hand value is " + str(dealer.get_value())
    outcome = "Hit or Stand?"
    return Score
def hit():
    global in_play, Score, outcome, game_over
    if in_play:
        player.add_card(game_deck.deal_card())
        print "player hand value is " + str(player.get_value())
        if player.hand_value <= 21:
            print str(player)
            print "Hit or Stand?"
            outcome = "Hit or Stand?"
        else:
            outcome = "You busted. Click deal to play again."
            in_play = False
            game_over = True
            Score -= 1
    return Score, outcome, in_play, game_over
    print game_over
def stand():
    global in_play, Score, outcome, game_over
    if not in_play:
        outcome = "Standing's not an option"
    else:
        while dealer.get_value() <= 17:
            print str(game_deck)
            dealer.add_card(game_deck.deal_card())
            print dealer.get_value()
        if dealer.hand_value >= player.hand_value and dealer.hand_value <=21:
            outcome = "You lose. Click deal to play again."
            Score -= 1
        else:
            outcome = "You win! Click Deal to play again."
            Score +=1
    in_play = False
    game_over = True
    return Score, outcome, in_play, game_over
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global Score, outcome
    # test to make sure that card.draw works, replace with your code below
    
#    card = Card("S", "A")
#    card.draw(canvas, [300, 300])
    player.draw(canvas, [75,150])
    dealer.draw(canvas, [75,350])
    canvas.draw_text(outcome, [200,140],25, "Black")
    canvas.draw_text("Blackjack", [150,50], 40, "skyblue")
    canvas.draw_text("Player", [72,140], 25, "Black")
    canvas.draw_text("Dealer", [72,340], 25, "Black")
    canvas.draw_text("Score = "+str(Score), [475,50], 25, "Black")
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
player = []
dealer = []
deal()
frame.start()


# remember to review the gradic rubric