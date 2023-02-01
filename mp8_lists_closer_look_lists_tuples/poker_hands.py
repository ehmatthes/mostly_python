from random import choice

all_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k', 'a']

def get_hand(hand_size=5):
    """Return a hand of cards."""
    return [choice(all_cards) for _ in range(hand_size)]

num_hands = 10
hands = [get_hand() for _ in range(num_hands)]

print(f"\nGenerated {len(hands):,} hands.")
print(hands[0])