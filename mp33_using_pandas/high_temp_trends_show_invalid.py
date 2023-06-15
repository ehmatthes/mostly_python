from pathlib import Path

import pandas as pd

def get_data(path):
    """Extract dates and high temperatures."""
    df = pd.read_csv(path)
    df['DATE'] = pd.to_datetime(df['DATE'])
    
    return df['DATE'], df['TMAX']

# Extract data.
path = Path('wx_data/sitka_highs_1944_2023.csv')
dates, highs = get_data(path)
print(f"\nFound {len(highs):,} data points.")

num_invalid = highs.isna().sum()
print(f"There are {num_invalid} invalid readings.")