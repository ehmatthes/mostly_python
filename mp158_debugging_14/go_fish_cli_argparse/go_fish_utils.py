"""Utility functions for the Go Fish game."""

from collections import Counter
import subprocess
import sys

from cli import cli_args


def get_player_guess(player_hand):
    """Get a valid guess from the player."""
    msg = "\nWhat card would you like to ask for? "
    requested_card = input(msg).upper()

    if requested_card == "QUIT":
        sys.exit("\nThanks for playing!")
    if requested_card not in "2345678910JQKA":
        print("Invalid entry, please try again.")
        return get_player_guess(player_hand)

    player_ranks = [c.rank for c in player_hand.cards]
    if requested_card not in player_ranks:
        print("You don't have that card!")
        return get_player_guess(player_hand)

    # Valid response.
    return requested_card

def remove_card(target_rank, hand):
    """Remove the first card with a matching rank, and return it."""
    for card in hand.cards:
        if card.rank == target_rank:
            hand.cards.remove(card)
            return card

def remove_pair(target_rank, hand):
    """Remove and return a pair of cards with a matching rank."""
    return (
        remove_card(target_rank, hand),
        remove_card(target_rank, hand),
    )

def check_pairs(hand, pairs, owner):
    """Check for pairs in a hand."""
    ranks = [c.rank for c in hand.cards]
    ranks_counts = Counter(ranks)
    for rank, count in ranks_counts.items():
        if count in (2, 3):
            # Remove first two of this rank, and add to pairs.
            pair = remove_pair(rank, hand)
            pairs.append(pair)
            pause(f"\nFound a pair in {owner} hand: {pair}\n")
        if count == 4:
            # There were four cards of the same rank. Remove second pair.
            pair = remove_pair(rank, hand)
            pairs.append(pair)
            pause(f"\nFound a pair in {owner} hand: {pair}\n")

def clear_terminal():
    """Clear the terminal."""
    # Don't clear terminal in verbose mode.
    if cli_args.verbose:
        return
        
    if sys.platform == "win32":
        subprocess.run("cls")
    else:
        subprocess.run("clear")

def pause(message):
    """Pause for player to see an update."""
    message += " Press Enter to continue."
    input(message)