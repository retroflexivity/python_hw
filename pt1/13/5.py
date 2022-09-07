import pandas as pd

df = pd.read_csv('nba.csv')

df.groupby('player_name')['net_rating'].mean().sort_values(ascending=False).reset_index().head(10)
