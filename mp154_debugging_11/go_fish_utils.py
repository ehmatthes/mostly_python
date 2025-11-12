"""Utility functions for the Go Fish game."""

import subprocess
import sys

def get_player_guess(player_hand):
    """Get a valid guess from the player."""
    msg = "\nWhat card would you like to ask for? "
    requested_card = input(msg).upper()

    if requested_card == "QUIT":
        sys.exit("\nThanks for playing!")
    if requested_card not in "2345678910JQKA":
        print("Invalid entry, please try again.")
        get_player_guess(player_hand)

    player_ranks = [c.rank for c in player_hand.cards]
    if requested_card not in player_ranks:
        print("You don't have that card!")
        get_player_guess(player_hand)

    # Valid response.
    return requested_card

def clear_terminal():
    """Clear the terminal."""
    if sys.platform == "win32":
        subprocess.run("cls")
    else:
        subprocess.run("clear")