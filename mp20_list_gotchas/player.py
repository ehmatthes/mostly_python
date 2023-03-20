"""Represent a player in a card game."""

class Player:

    def __init__(self, name, hand=[]):
        """Each player has a name, and a hand."""
        self.name = name
        self.hand = hand

    def show_cards(self):
        """Show all the cards in the current hand."""
        if self.hand:
            print(f"{self.name} has the following cards:")
            print(f"\t{self.hand}")
        else:
            print(f"{self.name} has no cards.")