"""Utility functions for dice_battle."""

from die import Die


def battle():
    """Run a single dice battle."""
    die = Die()

    a_result = die.roll()
    b_result = die.roll()
    return a_result, b_result


def update_results(a_result, b_result, results):
    """Update results after a battle."""
    if a_result > b_result:
        print("Player A won!")
        results["wins_a"] += 1
    elif b_result > a_result:
        print("Player B won!")
        results["wins_b"] += 1
    else:
        print("Tie!")
        results["ties"] += 1
        

def show_summary(results):
    """Show summary of all battles."""
    print("\n\nSummary:")
    print(f"  Player A won {results["wins_a"]} battles.")
    print(f"  Player B won {results["wins_b"]} battles.")
    print(f"  There were {results["ties"]} tied battles.")

    if results["wins_a"] > results["wins_b"]:
        print("\nClearly, player A is better at rolling dice.")
    elif results["wins_b"] > results["wins_a"]:
        print("\nClearly, player B is better at rolling dice.")
    else:
        print("\nClearly, player A and player B are equals.")