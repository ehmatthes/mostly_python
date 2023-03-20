from random import choice

def get_card():
    """Return a random card."""
    suits = ('\u2660', '\u2663', '\u2665', '\u2666')
    values = (
        '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'J', 'Q', 'K', 'A'
    )
    return choice(values) + choice(suits)