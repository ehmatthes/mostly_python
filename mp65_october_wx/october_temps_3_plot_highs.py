from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

path = Path('wx_data/sitka_temps_1983_2023.csv')
df_all = pd.read_csv(path)
df_all['DATE'] = pd.to_datetime(df_all['DATE'])

# Keep only October's data for each year.
df_october = df_all[df_all['DATE'].dt.month == 10]

# Visualize data.
fig, ax = plt.subplots(figsize=(10, 6))
title = "October 2023, Sitka AK"
ax.set_title(title, fontsize=18)
ax.set_xlabel("October __")
ax.set_ylabel("T (F)")

# Plot each year as a separate line.
for year in range(1983, 2024):
    df_current_year = df_october[df_october['DATE'].dt.year == year]
    dates = df_current_year['DATE']

    # Want integer days, not actual dates for plotting.
    days = df_current_year['DATE'].dt.day
    highs = df_current_year['TMAX']

    # Set line style by year.
    if year == 2023:
        ax.plot(days, highs, color='red', alpha=0.6)
    else:
        ax.plot(days, highs, color='gray', alpha=0.2)

plt.savefig("october_highs.png", bbox_inches="tight")