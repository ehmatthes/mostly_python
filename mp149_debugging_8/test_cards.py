from card_models import Card
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
