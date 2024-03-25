from dataclasses import dataclass
from pathlib import Path
import pdb

import pandas as pd

@dataclass
class Member:
    email: str = ""
    member_id: str = ""
    name: str = ""

path = Path("subscribers.csv")
subscriber_data = pd.read_csv(path)

emails = list(subscriber_data.email)
names = list(subscriber_data.name)

# Build a list of Members.
members = []
for email, name in zip(emails, names):
    member = Member()
    member.email = email
    member.name = name

    members.append(member)

breakpoint()
