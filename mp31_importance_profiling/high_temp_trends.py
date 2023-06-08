from pathlib import Path
import csv
from datetime import datetime

def get_data(path):
    """Extract dates and high temperatures."""
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        try:
            high = int(row[2])
            highs.append(high)
            current_date = datetime.strptime(row[1], '%Y-%m-%d')
            dates.append(current_date)
        except ValueError:
            print(row)

    return dates, highs

# Extract data.
path = Path('wx_data/sitka_highs_1944_2012.csv')
dates, highs = get_data(path)
print(f"\nFound {len(highs):,} data points.")