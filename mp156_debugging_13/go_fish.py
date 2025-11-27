"""Go Fish game, where one person plays against computer."""

import sys
import random

from card_models import Card, Hand, Deck
import go_fish_utils


class GoFish:

    def __init__(self):
        # Set a random seed if requested.
        if "--seed" in sys.argv:
            random.seed(42)

    def start_game(self):
        # Shuffle, and deal two hands.
        self.deck = Deck()
        self.deck.shuffle()
        go_fish_utils.clear_terminal()

        hands = self.deck.deal(num_hands=2, num_cards=7)
        self.player_hand, self.computer_hand = hands
        
        self.player_hand.organize()
        self.computer_hand.organize()

        self.player_pairs = []
        self.computer_pairs = []

        # Check for any pairs either player already has.
        go_fish_utils.check_pairs(self.player_hand, self.player_pairs, "your")
        go_fish_utils.check_pairs(self.computer_hand, self.computer_pairs, "computer's")

        # Player goes first.
        self.player_turn()

    def player_turn(self):
        """Manage the human player's turn."""
        go_fish_utils.clear_terminal()
        self.show_state()
        self.check_finished()
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
            go_fish_utils.pause("\nYour guess was correct!")
            self.player_turn()
        else:
            # It's the computer's turn now.
            go_fish_utils.pause("\nYour guess was incorrect.")
            new_card = self.deck.draw()
            go_fish_utils.pause(f"\nYou drew: {new_card}.\n")

            self.player_hand.cards.append(new_card)
            self.player_hand.organize()
            go_fish_utils.check_pairs(self.player_hand, self.player_pairs, "your")

            self.computer_turn()
    
    def computer_turn(self):
        """Manage the computer's turn."""
        go_fish_utils.clear_terminal()
        self.show_state()
        self.check_finished()
        requested_card = random.choice(self.computer_hand.cards).rank
        self.check_computer_guess(requested_card)

    def check_computer_guess(self, guessed_rank):
        """Process the computer's guess."""
        msg = f"\nThe computer asked for a {guessed_rank}."
        print(msg)

        player_ranks = [c.rank for c in self.player_hand.cards]
        if guessed_rank in player_ranks:
            # Correct guess. Remove card from both hands.
            player_card = go_fish_utils.remove_card(
                guessed_rank, self.player_hand)
            computer_card = go_fish_utils.remove_card(
                guessed_rank, self.computer_hand)

            # Add cards to computer's pairs.
            self.computer_pairs.append((player_card, computer_card))

            # Computer gets to go again.
            go_fish_utils.pause("\nThe computer's guess was correct!")
            self.computer_turn()
        else:
            # It's the player's turn now.
            go_fish_utils.pause("The computer's guess was incorrect.")
            new_card = self.deck.draw()
            if "-v" in sys.argv:
                go_fish_utils.pause(f"Computer drew: {new_card}.\n")
            else:
                go_fish_utils.pause("The computer drew a card.")

            self.computer_hand.cards.append(new_card)
            self.computer_hand.organize()
            go_fish_utils.check_pairs(
                self.computer_hand, self.computer_pairs, "computer's")

            self.player_turn()

    def show_state(self):
        """Show the current state of the game."""
        msg = f"Player pairs:   {len(self.player_pairs)}"
        msg += f"\nComputer pairs: {len(self.computer_pairs)}"
        print(msg)

        print("\nPlayer hand:")
        self.player_hand.show()

        print("\nComputer hand:")
        if "-v" in sys.argv:
            self.computer_hand.show()
        else:
            self.computer_hand.show(hidden=True)

    def check_finished(self):
        """Check if the game is over."""
        # If both hands have at least one card, game is not over.
        if self.player_hand.cards and self.computer_hand.cards:
            return

        # Announce the winner.
        if not self.player_hand.cards and not self.computer_hand.cards:
            msg = "\nTie game!\n\n"
        if not self.player_hand.cards:
            msg = "\nYou won!!!\n\n"
        else:
            msg = "\nThe computer won. :/\n\n"
        go_fish_utils.pause(msg)

        # Play again?
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() in ("y", "yes"):
            self.start_game()
        else:
            print("Thanks for playing!")
            sys.exit()

if __name__ == "__main__":
    gf_game = GoFish()
    gf_game.start_game()