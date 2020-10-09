import random
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Incorrect input"
    # convert name to number using if/elif/else
    # don't forget to return the result!
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Incorrect input"
    # convert number to a name using if/elif/else
    # don't forget to return the result!
def rpsls(player_choice):
    print
    # print a blank line to separate consecutive games
    print "Player chooses ", player_choice
    # print out the message for the player's choice
    player_number = name_to_number(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    comp_number = random.randrange(0,5)
    # compute random guess for comp_number using random.randrange()
    comp_choice = number_to_name(comp_number)
    print "Computer chooses ", comp_choice
    # convert comp_number to comp_choice using the function number_to_name()
    # print out the message for computer's choice
    # compute difference of comp_number and player_number modulo five
    if (comp_number - player_number) < 0:
        print "Player wins!"
    elif (comp_number - player_number) == 1 or (comp_number - player_number) == 2:
        print "Computer wins!"
    elif (comp_number - player_number) > 2:
        print "Player wins!"
    else:
        print "Tie:)"
    # use if/elif/else to determine winner, print winner message
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
