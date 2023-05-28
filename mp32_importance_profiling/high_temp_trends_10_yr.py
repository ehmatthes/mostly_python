from pathlib import Path
import csv, statistics
from datetime import datetime

import matplotlib.pyplot as plt

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

def get_averages(temps, timespan):
    # Calc moving averages over the entire dataset.
    avgs = []
    for index in range(timespan, len(temps)):
        temps_slice = temps[index-timespan:index]
        mean = statistics.mean(temps_slice)
        avgs.append(mean)

    return avgs

def plot_data(dates, temps, title="",
        filename="output/high_temps.png"):
    """Plot daily temperature data."""
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(20, 6))

    ax.plot(dates, temps, color='red', alpha=0.6)

    # Format plot.
    ax.set_title(title, fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)

    plt.savefig(filename, bbox_inches="tight")

# Extract data.
path = Path('wx_data/sitka_highs_1944_2012.csv')
dates, highs = get_data(path)
print(f"\nFound {len(highs):,} data points.")

# Analyze data.
timespan = 10 * 365
avgs = get_averages(highs, timespan=timespan)

# Plot the data.
title = f"{int(timespan/365)}-year Moving Average Temperature"
relevant_dates = dates[timespan:]
plot_data(relevant_dates, avgs, title)