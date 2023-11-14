from pathlib import Path
import pandas as pd

path = Path('wx_data/sitka_temps_1983_2023.csv')
df_all = pd.read_csv(path)
df_all['DATE'] = pd.to_datetime(df_all['DATE'])

# Keep only October's data for each year.
df_october = df_all[df_all['DATE'].dt.month == 10]

dates = df_october['DATE']
highs = df_october['TMAX']

print(dates[:5], highs[:5])