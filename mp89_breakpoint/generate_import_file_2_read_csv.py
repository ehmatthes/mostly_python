from dataclasses import dataclass
from pathlib import Path

import pandas as pd

@dataclass
class Member:
    email: str = ""
    member_id: str = ""
    name: str = ""

path = Path("subscribers.csv")
subscriber_data = pd.read_csv(path)