from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

def get_data(path):
    """Extract dates and high temperatures."""
    df = pd.read_csv(path)
    df['DATE'] = pd.to_datetime(df['DATE'])

    df.dropna(inplace=True)
    
    return df['DATE'], df['TMAX']

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
path = Path('wx_data/sitka_highs_1944_2023.csv')
dates, highs = get_data(path)
print(f"\nFound {len(highs):,} data points.")

# Analyze data.
num_years = 30
timespan = num_years * 365
avgs = highs.rolling(timespan).mean()

# Plot the data.
title = f"{num_years}-year Moving Average Temperature"

filename = f"output/high_temps_{num_years}_year_moving_average.png"
plot_data(dates, avgs, title, filename=filename)

print(f"  Generated plot: {filename}")