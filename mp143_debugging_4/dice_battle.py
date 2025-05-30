"""Simulate a game of rolling dice.

Two players take turns rolling dice, and see who
rolls a higher number.
"""

import utils


# Simulate some battles between players A and B.
num_battles = 10
results = {
    "wins_a": 0,
    "wins_b": 0,
    "ties": 0,
}

for _ in range(num_battles):
    a_result, b_result = utils.battle()
    print(f"\nPlayer A: {a_result}")
    print(f"Player B: {b_result}")

    utils.update_results(a_result, b_result, results)

utils.show_summary(results)
