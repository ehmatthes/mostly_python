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

ace_spades = Card("A", "spades")
ace_clubs = Card("A", "clubs")
ten_spades = Card("10", "spades")
