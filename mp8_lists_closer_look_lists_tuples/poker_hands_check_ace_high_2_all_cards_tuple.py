from random import choice

all_cards = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k', 'a')

def get_hand(hand_size=5):
    """Return a hand of cards."""
    return [choice(all_cards) for _ in range(hand_size)]

def check_ace_high_straight(hand):
    """Check if hand is an ace-high straight."""
    for card in [10, 'j', 'q', 'k', 'a']:
        if card not in hand:
            return False
    return True

num_hands = 5_000_000
hands = [get_hand() for _ in range(num_hands)]

print(f"\nGenerated {len(hands):,} hands.")
print(hands[0])

# Check for any ace-high straights.
winners = []
for hand in hands:
    if check_ace_high_straight(hand):
        winners.append(hand)

if winners:
    print(f"\nFound {len(winners)} winning hands.")
    print(winners[0])
else:
    print("\nNo winning hands found.")