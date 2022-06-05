import pandas as pd

df = pd.read_csv('nba.csv')

# 1
df[df['draft_round'] != 'Undrafted'].groupby('draft_round')['player_height'].min()

# 2
df[df['draft_round'] != 'Undrafted'].groupby('draft_round')['player_weight'].apply(lambda x: x.max() - x.min()).idxmax()
