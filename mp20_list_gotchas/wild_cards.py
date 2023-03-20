hand = ['5♦', '4♣', 'w', '5♦', 'A♣', 'w', '3♥', 'w']
print(hand)

while 'w' in hand:
    hand.remove('w')
    
print(hand)