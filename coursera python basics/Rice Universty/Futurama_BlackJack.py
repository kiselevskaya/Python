# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("https://www.dropbox.com/s/eau13fd8bpf7vxq/Futurama_Deck.png?dl=1")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
#card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")
card_back = simplegui.load_image("https://www.dropbox.com/s/hpg6n00k5wlmika/Deck_back.png?dl=1")

background_size = (830, 600)
background_center = (415, 300)
    #background = simplegui.load_image("https://www.dropbox.com/s/hxwclrhfdveqg3j/planet_express.jpg?dl=1")
background = simplegui.load_image("https://www.dropbox.com/s/4ejm4y8ex2ofvs8/Planet_Express.png?dl=1")
    #background = simplegui.load_image("https://www.dropbox.com/s/nxjtf613zpt6e7b/RedDwarfPlanet.png?dl=1")
    #background = simplegui.load_image("https://www.dropbox.com/s/u5ztanit5okwn6h/01acv04_038.png?dl=1")
    #background = simplegui.load_image("https://www.dropbox.com/s/hmf4lpy2wbsqoxl/Leela.png?dl=1")

#bender_size = (110, 200)
#bender_centre = (55, 100)
#bender = simplegui.load_image("https://www.dropbox.com/s/13otxb25fq7zdbq/bender.png?dl=1")

#the_botfather_size = (110, 200)
#the_botfather_centre = (55, 100)
#the_botfather = simplegui.load_image("https://www.dropbox.com/s/uhfujh6mr3j7tof/Rich_Bender.png?dl=1")

bender_size = (120, 153)
bender_centre = (60, 76.5)
bender = simplegui.load_image("https://www.dropbox.com/s/3iyxcq0m4h4sy7b/bender_nibbler.png?dl=1")

the_botfather_size = (100, 167)
the_botfather_centre = (50, 83.5)
the_botfather = simplegui.load_image("https://www.dropbox.com/s/vquyxrklagpz6cx/Botfather.png?dl=1")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
bender_win = None
stand_on = False

plus_list = ["I don't blame myself. I blame all of you!",
    "It ain't easy. It just proves how great I am!", "You bastard!",
    "I'm an expert at not caring!",
    "Hey sexy mama, wanna kill all humans?",
    "I'll go build my own lunar lander, with blackjack and hookers!",
    "I'm so embarrassed. I wish everybody else was dead!"]
minus_list = ["Game's over, loser! I have all the money!",
    "Compare your life to mine and then kill yourself. Haha!",
    "Hasta la vista, meatbag!",
    "You know what cheers me up? Other people's misfortune!",
    "Hahahaha. Oh wait you're serious. Let me laugh even harder!",
    "Bite my shiny metal ass!"]

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
        self.collection = []

    def __str__(self):
        s = "Hend contains "
        for item in range(len(self.collection)):
            s += self.collection[item].suit + self.collection[item].rank + " "
        return s

    def add_card(self, card):
        self.collection.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hend_value = 0
        for item in range(len(self.collection)):
            hend_value += VALUES[self.collection[item].rank]
        for item in range(len(self.collection)):
            if VALUES[self.collection[item].rank] == 1:
                if (hend_value + 10) <= 21:
                    hend_value += 10
        return hend_value

    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for c in self.collection:
            c.draw(canvas, pos)
            pos[0] += 96

# define deck class
class Deck:
    def __init__(self):
        self.deck_list = []
        for item in SUITS:
            for element in RANKS:
                card = Card(item, element) # str(item) + str(element)
                self.deck_list.append(card)

    def shuffle(self):
        random.shuffle(self.deck_list)

    def deal_card(self):
        self.card = self.deck_list.pop(0) # Card(random.choice(SUITS), random.choice(RANKS))
        return self.card

    def __str__(self):
        s = "Deck contains "
        for item in range(len(self.deck_list)):
            s += self.deck_list[item] + " "
        return s

#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck, score, minus_list, bender_win, stand_on

    if in_play:
        score -= 1
        outcome = random.choice(minus_list)
        in_play = False
        bender_win = True
        stand_on = True

    # your code goes here
    else:
        deck = Deck()
        deck.shuffle()
        bender_win = None
        stand_on = False

        player = Hand()
        dealer = Hand()

        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())

        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        print "Player has: " + str(player)
        print "Dealer has: " + str(dealer)
        in_play = True
        outcome = "Hit or Stand?"

def hit():
    # replace with your code below
    global outcome, in_play, player, dealer, deck, score, minus_list, bender_win, stand_on
    # if the hand is in play, hit the player

    if in_play:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
        print "Player has: " + str(player)
    # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            in_play = False
            print "You have busted"
            score -= 1
            bender_win = True
            outcome = random.choice(minus_list)
            stand_on = True

def stand():

    # replace with your code below
    global outcome, in_play, player, dealer, deck, score, plus_list, bender_win, stand_on
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while stand_on is False:

        in_play = False
        outcome = "You have busted! New deal!?"
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        print "Dealer has: " + str(dealer)
        # assign a message to outcome, update in_play and score
        if dealer.get_value() > 21:
            print "Dealer has busted"
            score += 1
            bender_win = False
            print "Player has won!"
            outcome = random.choice(plus_list)
        else:
            if player.get_value() > 21 or player.get_value() <= dealer.get_value():
                score -= 1
                bender_win = True
                print "Player lost!"
                outcome = random.choice(minus_list)
            else:
                print "Player won!"
                score += 1
                bender_win = False
                outcome = random.choice(plus_list)
        stand_on = True

# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_image(background, background_center,
        background_size, background_center, background_size)

    player.draw(canvas, [24, 410])
    dealer.draw(canvas, [24, 120])
    canvas.draw_text("BlackJack", [36, 80], 80, "Maroon")
    canvas.draw_text(str(score), [700, 110], 100, "Maroon")
    canvas.draw_text(outcome, [130, 290], 28, "DarkCyan")

    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
            [24 + CARD_BACK_CENTER[0], 120 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    else:
        if bender_win is True:
            canvas.draw_image(the_botfather, the_botfather_centre, the_botfather_size, [60, 300], the_botfather_size)
        elif bender_win is False:
            canvas.draw_image(bender, bender_centre, bender_size, [65, 300], bender_size)

# initialization frame
frame = simplegui.create_frame("Blackjack", 830, 600)
#frame.set_draw_handler(draw_handler)
frame.set_canvas_background("DarkGreen")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
