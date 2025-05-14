import random
import os
from dataclasses import dataclass


# Set a random seed when testing.
if seed := os.environ.get("DICE_BATTLE_RANDOM_SEED"):
    random.seed(int(seed))


@dataclass
class Die:
    """Model a single die."""

    num_sides: int = 6

    def roll(self):
        """Roll the die."""
        return random.randint(1, self.num_sides)