from player import Player
from dealer import get_card

eric = Player('Eric')
kyle = Player('Kyle')

eric.show_cards()
kyle.show_cards()

for _ in range(5):
    new_card = get_card()
    eric.hand.append(new_card)

    new_card = get_card()
    kyle.hand.append(new_card)

eric.show_cards()
kyle.show_cards()