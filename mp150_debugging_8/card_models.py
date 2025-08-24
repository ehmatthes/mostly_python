import random
from operator import attrgetter

import card_data

class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        symbol = card_data.suits_symbols[self.suit]
        return f"{self.rank}{symbol}"

    def __eq__(self, card_2):
        """Two cards are equal if their ranks match."""
        return self.rank == card_2.rank

    def __gt__(self, card_2):
        """A card is greater if its value is higher."""
        return self.value > card_2.value

    def __lt__(self, card_2):
        """A card is lesser if its value is lesser."""
        return self.value < card_2.value

    @property
    def value(self):
        """Get a numerical value for the card."""
        return card_data.ranks_values[self.rank]

def same_suit(cards):
    """Check if all cards have the same suit."""
    suits = [c.suit for c in cards]
    return len(set(suits)) == 1

class Hand:

    def __init__(self, cards=None):
        if cards:
            self.cards = cards
        else:
            self.cards = []

    def organize(self):
        """Put cards in a more usable order."""
        self.cards.sort(key=attrgetter("value", "suit"))

    def show(self):
        hand_string = " ".join([str(card) for card in self.cards])
        print(hand_string)

class Deck:
    """Bottom of the deck is the start of the list, top of the deck is the end
    This makes drawing a card efficient.
    """

    def __init__(self):
        self.cards = []
        self.reset_deck()

    def reset_deck(self):
        """Build a standard, unshuffled deck."""
        ranks = card_data.ranks_values.keys()
        suits = card_data.suits_symbols.keys()

        for rank in ranks:
            for suit in suits:
                card = Card(rank, suit)
                self.cards.append(card)

    def show(self):
        deck_string = " ".join([str(card) for card in self.cards])
        print(deck_string)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, num_cards=1):
        """Draw one or more cards from top of the deck.
        Return a single card, or a list of cards.
        """
        if num_cards == 1:
            return self.cards.pop()

        return [self.cards.pop() for _ in range(num_cards)]

    def deal(self, num_hands=2, num_cards=5):
        """Return a single Hand, or list of Hands."""
        # Build empty hands.
        hands = [Hand() for _ in range(num_hands)]

        # Add cards to each hand, one at a time.
        for _ in range(num_cards):
            for hand in hands:
                hand.cards.append(self.draw())

        if len(hands) == 1:
            return hands[0]

        return hands