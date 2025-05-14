import os

import pytest


# --- Fixtures ---


@pytest.fixture(autouse=True, scope="session")
def set_random_seed_env():
    """Make random selections repeatable."""
    # To verify a random action, set autouse to False and run one test.
    os.environ["DICE_BATTLE_RANDOM_SEED"] = "10"