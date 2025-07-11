from datetime import datetime

import pandas as pd

# End date for players who are still living.
today = datetime.today().strftime("%m/%d/%Y")

df = pd.DataFrame([
    {"name": "Buddy Guy", "start": "6/30/1936", "end": today},
    {"name": "Buddy Holly", "start": "9/7/1936", "end": "2/3/1959"},
    {"name": "Ritchie Valens", "start": "5/13/1941", "end": "2/3/1959"},
    {"name": "Jimi Hendrix", "start": "11/24/1942", "end": "9/18/1970"},
    {"name": "Jeff Beck", "start": "6/24/1944", "end": "1/10/2023"},
    {"name": "Eric Clapton", "start": "3/30/1945", "end": today},
    {"name": "Ritchie Blackmore", "start": "4/14/1945", "end": today},
    {"name": "David Gilmour", "start": "3/6/1946", "end": today},
    {"name": "Rory Gallagher", "start": "3/2/1948", "end": "6/14/1995"},
    {"name": "Mark Knopfler", "start": "8/12/1949", "end": today},
    {"name": "Bonnie Raitt", "start": "11/8/1949", "end": today},
    {"name": "Gary Moore", "start": "4/4/1952", "end": "2/6/2011"},
    {"name": "Stevie Ray Vaughan", "start": "10/3/1954", "end": "8/27/1990"},
    {"name": "Eric Johnson", "start": "8/17/1954", "end": today},
    {"name": "Dave Murray", "start": "12/23/1956", "end": today},
    {"name": "Yngwie Malmsteen", "start": "6/30/1963", "end": today},
    {"name": "Kurt Cobain", "start": "2/20/1967", "end": "4/5/1994"},
    {"name": "Ana Popović", "start": "5/13/1976", "end": today},
    {"name": "John Mayer", "start": "10/16/1977", "end": today},
])
