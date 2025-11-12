"""Go Fish game, where one person plays against computer."""

from card_models import Card, Hand, Deck


class GoFish:

    def __init__(self):
        # Start with a new shuffled deck.
        self.deck = Deck()
        self.deck.shuffle()

    def start_game(self):
        # Deal two hands.
        hands = self.deck.deal(num_hands=2, num_cards=7)
        self.player_hand, self.computer_hand = hands
        
        self.player_hand.organize()
        self.computer_hand.organize()

        self.player_pairs = []
        self.computer_pairs = []

        # Player goes first.
        self.player_turn()

    def player_turn(self):
        """Manage the human player's turn."""
        self.show_state()

        # Get player's guess (a rank).
        msg = "\nWhat card would you like to ask for? "
        requested_card = input(msg).upper()

        if requested_card == "QUIT":
            sys.exit("\nThanks for playing!")
        if requested_card not in "2345678910JQKA":
            print("Invalid entry, please try again.")
            self.player_turn()
            
        player_ranks = [c.rank for c in self.player_hand.cards]
        if requested_card not in player_ranks:
            print("You don't have that card!")
            self.player_turn()

    def show_state(self):
        """Show the current state of the game."""
        print("Player hand:")
        self.player_hand.show()

        print("\nComputer hand:")
        self.computer_hand.show(hidden=True)

if __name__ == "__main__":
    gf_game = GoFish()
    gf_game.start_game()