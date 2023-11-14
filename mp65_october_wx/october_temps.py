from pathlib import Path
import pandas as pd

path = Path('wx_data/sitka_temps_1983_2023.csv')
df = pd.read_csv(path)
df['DATE'] = pd.to_datetime(df['DATE'])

dates = df['DATE']
highs = df['TMAX']

print(dates[:5], highs[:5])