from card_models import Card, Hand, Deck
import card_models as cm


# --- Card tests ---

def test_create_card():
    """Make sure cards can be created in intended ways."""
    card = Card("2", "clubs")
    assert card.rank == "2"
    assert card.suit == "clubs"
    assert card.value == 2

def test_comparisons():
    """Test equality, gt, and lt comparisons."""
    ace_diamonds = Card(rank="A", suit="diamonds")
    ace_spades = Card(rank="A", suit="spades")
    seven_clubs = Card(rank="7", suit="clubs")

    # Equality
    assert ace_diamonds == ace_spades
    assert ace_diamonds != seven_clubs

    # GT
    assert ace_diamonds > seven_clubs
    assert not seven_clubs > ace_diamonds

    # LT
    assert seven_clubs < ace_diamonds
    assert not ace_diamonds < seven_clubs

def test_same_suit_comparison():
    """Test same_suit() method."""
    ace_diamonds = Card(rank="A", suit="diamonds")
    two_diamonds = Card(rank="2", suit="diamonds")
    three_diamonds = Card(rank="3", suit="diamonds")
    four_clubs = Card(rank="7", suit="clubs")

    # Check with individual cards.
    assert cm.same_suit([ace_diamonds, two_diamonds])
    assert cm.same_suit([ace_diamonds, two_diamonds, three_diamonds])
    assert not cm.same_suit([ace_diamonds, four_clubs])


# --- Hand tests ---

def test_organize_hand():
    hand = Hand([
        Card("9", "hearts"),
        Card("3", "clubs"),
        Card("9", "spades"),
        Card("K", "diamonds"),
        Card("7", "spades"),
        ])

    hand.organize()

    assert hand.cards[0].rank == "3" and hand.cards[0].suit == "clubs"
    assert hand.cards[1].rank == "7" and hand.cards[1].suit == "spades"
    assert hand.cards[2].rank == "9" and hand.cards[2].suit == "hearts"
    assert hand.cards[3].rank == "9" and hand.cards[3].suit == "spades"
    assert hand.cards[4].rank == "K" and hand.cards[4].suit == "diamonds"


# --- Deck tests ---

def test_starting_deck():
    deck = Deck()

    # Check deck length.
    assert len(deck.cards) == 52

    # Check first and last cards.
    assert deck.cards[0].rank == "2"
    assert deck.cards[0].suit == "spades"
    assert deck.cards[-1].rank == "A"
    assert deck.cards[-1].suit == "clubs"

    # Check all cards unique.
    # Can't use set without defining __hash__(), which I don't want to do.
    # Keep it simple, and not sure what mixing decks would look like.
    ranks_suits = [c.rank + c.suit for c in deck.cards]
    assert len(set(ranks_suits)) == 52

def test_shuffle():
    """Note: this will sometimes fail, without a random seed."""
    deck = Deck()
    deck.shuffle()

    # Shouldn't often see same first and last cards.
    assert not all([
        deck.cards[0].rank == "2",
        deck.cards[0].suit == "spades",
        deck.cards[-1].rank == "A",
        deck.cards[-1].suit == "clubs",
    ])

def test_draw():
    """Draw a few cards from a fresh deck."""
    deck = Deck()

    card = deck.draw()
    assert card.rank == "A"
    assert card.suit == "clubs"

    card = deck.draw()
    assert card.rank == "A"
    assert card.suit == "diamonds"

def test_draw_multiple():
    """Draw multiple cards at once."""
    deck = Deck()
    cards = deck.draw(5)

    assert len(cards) == 5
    assert len(deck.cards) == 47

def test_deal():
    """Test dealing two hands of three cards each."""
    deck = Deck()
    hand_1, hand_2 = deck.deal(num_hands=2, num_cards=3)

    # Check hand and deck lengths.
    assert len(hand_1.cards) == len(hand_2.cards) == 3
    assert len(deck.cards) == 46

    # Check hand_1 contents.
    assert hand_1.cards[0].rank == "A" and hand_1.cards[0].suit == "clubs"
    assert hand_1.cards[1].rank == "A" and hand_1.cards[1].suit == "hearts"
    assert hand_1.cards[2].rank == "K" and hand_1.cards[2].suit == "clubs"

def test_deal_single_hand():
    """Test dealing a single hand of three cards."""
    deck = Deck()
    hand = deck.deal(num_hands=1, num_cards=3)

    # Check hand and deck lengths.
    assert len(hand.cards) == 3
    assert len(deck.cards) == 49

    # Check hand contents.
    assert hand.cards[0].rank == "A" and hand.cards[0].suit == "clubs"
    assert hand.cards[1].rank == "A" and hand.cards[1].suit == "diamonds"
    assert hand.cards[2].rank == "A" and hand.cards[2].suit == "hearts"