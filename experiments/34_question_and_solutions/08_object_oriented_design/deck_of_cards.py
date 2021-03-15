# deck_of_cards.py


import itertools
import random


"""
Design the data structure for a generic deck of cards.
Explain how you would subclass the data structures to implement blackjack.

Assume the generic deck is regular 52 cards deck.
"""


class Deck:
    def __init__(self):
        self.deck = list(itertools.product([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'], ['Spade', 'Heart', 'Diamond', 'Club']))
        self.card = 0

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if self.card == 52:
            return 'The Deck is empty'
        card = self.deck[self.card]
        self.card += 1
        print(card)
        return card


class Hand:
    def __init__(self):
        self.hand = []
        self.score = 0

    def add_to_hand(self, card):
        self.hand.append(card)
        self.add_score(card[0])

    def add_score(self, value):
        if isinstance(value, int):
            self.score += value
        elif value == 'A':
            # Ace could be 1 or 11
            self.score += 1
            if self.score + 10 <= 21:
                self.score += 10
        else:
            self.score += 10

    def get_score(self):
        return self.score


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    while hand.get_score() < 21:
        hand.add_to_hand(deck.deal())
    print(hand.get_score())


