"""Simulate a game of rolling dice.

Two players take turns rolling dice, and see who
rolls a higher number.
"""
import random
from dataclasses import dataclass

@dataclass
class Die:
    """Model a single die."""

    num_sides: int = 6

    def roll(self):
        """Roll the die."""
        return random.randint(1, self.num_sides)

# Make one die that both players will share.
die = Die()

# Simulate some battles between players A and B.
num_battles = 10
wins_a, wins_b, ties = 0, 0, 0
for _ in range(num_battles):
    a_result = die.roll()
    b_result = die.roll()
    print(f"\nPlayer A: {a_result}")
    print(f"Player B: {b_result}")

    if a_result > b_result:
        print("Player A won!")
        wins_a += 1
    elif b_result > a_result:
        print("Player B won!")
        wins_b += 1
    else:
        print("Tie!")
        ties += 1

# Show a summary.
print("\n\nSummary:")
print(f"  Player A won {wins_a} battles.")
print(f"  Player B won {wins_b} battles.")
print(f"  There were {ties} tied battles.")

if wins_a > wins_b:
    print("\nClearly, player A is better at rolling dice.")
elif wins_b > wins_a:
    print("\nClearly, player B is better at rolling dice.")
else:
    print("\nClearly, player A and player B are equals.")
