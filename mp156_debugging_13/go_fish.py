"""Go Fish game, where one person plays against computer."""

from collections import Counter
import sys
import random

from card_models import Card, Hand, Deck
import go_fish_utils


class GoFish:

    def __init__(self):
        # Start with a new shuffled deck.
        if "--seed" in sys.argv:
            random.seed(42)
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

        # Check for any pairs either player already has.
        self.check_pairs()

        # Player goes first.
        self.player_turn()

    def check_pairs(self):
        """Check for pairs in either player's hand."""
        # Player's hand.
        ranks = [c.rank for c in self.player_hand.cards]
        ranks_counts = Counter(ranks)
        for rank, count in ranks_counts.items():
            if count in (2, 3):
                # Remove first two of this rank, and add to player_pairs.
                card_1 = go_fish_utils.remove_card(rank, self.player_hand)
                card_2 = go_fish_utils.remove_card(rank, self.player_hand)
                pair = (card_1, card_2)
                self.player_pairs.append(pair)
            if count == 4:
                # Player had all four cards of the same rank. Remove second pair.
                card_1 = go_fish_utils.remove_card(rank, self.player_hand)
                card_2 = go_fish_utils.remove_card(rank, self.player_hand)
                pair = (card_1, card_2)
                self.player_pairs.append(pair)

    def player_turn(self):
        """Manage the human player's turn."""
        go_fish_utils.clear_terminal()
        self.show_state()
        requested_card = go_fish_utils.get_player_guess(
            self.player_hand)
        self.check_player_guess(requested_card)

    def check_player_guess(self, guessed_rank):
        """Process the player's guess."""
        computer_ranks = [c.rank for c in self.computer_hand.cards]
        if guessed_rank in computer_ranks:
            # Correct guess. Remove card from both hands.
            player_card = go_fish_utils.remove_card(
                guessed_rank, self.player_hand)
            computer_card = go_fish_utils.remove_card(
                guessed_rank, self.computer_hand)

            # Add cards to player's pairs.
            self.player_pairs.append((player_card, computer_card))

            # Player gets to go again.
            msg = "\nYour guess was correct!"
            msg += " Press Enter to continue."
            input(msg)
            self.player_turn()
        else:
            # It's the computer's turn now.
            pass

    def show_state(self):
        """Show the current state of the game."""
        print("Player hand:")
        self.player_hand.show()

        print("\nComputer hand:")
        if "-v" in sys.argv:
            self.computer_hand.show()
        else:
            self.computer_hand.show(hidden=True)

if __name__ == "__main__":
    gf_game = GoFish()
    gf_game.start_game()