# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global num_range
    global upper
    global lower
    range100()

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global secret_number
    global num_range
    global upper
    global lower
    lower = 0
    upper = 100
    num_range = int(math.ceil(math.log((upper - lower + 1), 2)))
    secret_number = random.randrange(0, 100)
    print "New game. Range is " + "[" + str(lower) + ", " + str(upper) + ")"
    print "Number of remaining guesses is ", num_range
    print
    return secret_number, num_range, upper, lower
    # remove this when you add your code
    #ass

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global secret_number
    global num_range
    global upper
    global lower
    lower = 0
    upper = 1000
    num_range = int(math.ceil(math.log((upper - lower + 1), 2)))
    secret_number = random.randrange(0, 1000)
    print "New game. Range is " + "[" + str(lower) + ", " + str(upper) + ")"
    print "Number of remaining guesses is ", num_range
    print
    return secret_number, num_range, upper, lower
    #pass

def input_guess(guess):
    # main game logic goes here
    player_guess = int(guess)
    print "Guess was ", player_guess
    global secret_number
    global num_range
    global upper
    global lower
    if (player_guess >= upper or player_guess < lower) and  num_range >= 0:
        print "Out of range!"
        print
    elif player_guess > secret_number and  num_range >= 0:
        num_range = num_range - 1
        print "Number of remaining guesses is ", num_range
        print "Lower!"
        print
    elif player_guess < secret_number and  num_range >= 0:
        num_range = num_range - 1
        print "Number of remaining guesses is ", num_range
        print "Higher!"
        print
    elif player_guess == secret_number and  num_range >= 0:
        num_range = num_range - 1
        print "Number of remaining guesses is ", num_range
        print "Correct!"
        print
        new_game()
    else:
        print "You ran out of guesses. The number was ", secret_number
        print
        new_game()


    # remove this when you add your code
    #pass


# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_button("Range is [0; 100)", range100, 200)
frame.add_button("Range is [0; 1000)", range1000, 200)
frame.add_input("Enter your guess...", input_guess, 200)
# register event handlers for control elements and start frame
frame.start()

# call new_game
new_game()


# always remember to check your completed program against the grading rubric
