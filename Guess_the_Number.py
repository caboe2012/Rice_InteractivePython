# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
from random import randrange
secret_number = 0
count = 0
upper_bound = 100
print "Welcome to Guess the Number!"
print "Choose a number between 0 and 99, inclusive."
print "Or, click the 0 to 1000 button for a real challenge!"
print
# helper function to start and restart the game
def new_game():
    global secret_number, count, upper_bound
    secret_number = randrange(0,upper_bound)
    if upper_bound == 100:
        count = 7
    else:
        count = 10
#    print "secret number is", secret_number
#    print "upper bound is" , upper_bound
#    print "count is", count
    print
# define event handlers for control panel
def range100():
    global upper_bound
    upper_bound = 100
    print "You have selected to start a new game."
    print "You have 7 chances to guess a number between 0 and 99."
    print "Please enter your guess"
    print
    new_game()
def range1000():
    global upper_bound
    upper_bound = 1000
    print "You have selected to start a new game."
    print "You have 10 chances to guess a number between 0 and 999."
    print "Please enter your guess"
    print
    new_game()

def input_guess(guess):
    global count
    guess = int(guess)
    print "Guess was", guess
    if guess < secret_number:
        count-=1
        print "Higher"
        print "You have %s tries remaining" % (count)
        print
        if count == 0:
            print "Sorry, you have no guesses left!"
            print "Don't worry, you get to play again right now!"
            print "Staring a new game."
            print
            print "Please guess a new number in the same range."
            print
            new_game()
    elif guess > secret_number:
        print "Lower"
        count-=1
        print "You have %s tries remaining" % (count)
        print
        if count == 0:
            print "Sorry, you have no guesses left!"
            print "Don't worry, you get to play again right now!"
            print "Staring a new game."
            print
            print "Please guess a new number in the same range."
            print
            new_game()
    else:
        print "Correct, you win!"
        print "Your reward is to play again!"
        print "Starting a new game now."
        print
        print "Try and guess the new number in the same range"
        print
        new_game()
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)
# register event handlers for control elements and start frame
frame.add_input("Input your guess below", input_guess, 100)
frame.add_button("Range:0-100", range100)
frame.add_button("Range:0-1000", range1000)
# call new_game 
new_game()
# always remember to check your completed program against the grading rubric
