from card_models import Card, Hand, Deck

cards = [
    Card("A", "spades"),
    Card("A", "clubs"),
    Card("10", "spades"),
    Card("7", "diamonds"),
    Card("K", "clubs"),
]

print("A simple hand:")
hand = Hand(cards)
hand.show()

print("\nOrganized hand:")
hand.organize()
hand.show()

print("\nA fresh deck:")
deck = Deck()
deck.show()

print("\nA shuffled deck:")
deck.shuffle()
deck.show()

print("\nDraw a single card:")
card = deck.draw()
print(card)

print("\nDraw five cards to make a hand:")
cards = deck.draw(5)
hand = Hand(cards)
hand.organize()
hand.show()

print("\nDealing two hands of seven cards:")
hands = deck.deal(num_hands=2, num_cards=7)
for hand in hands:
    hand.organize()
    hand.show()