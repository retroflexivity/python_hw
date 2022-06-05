import pandas as pd

df = pd.read_csv('nba.csv')
df.head(1)

round1_mean = df[df['draft_round'] == '1']['pts'].mean()

# 1
df[(df['draft_round'] == '2') & (df['pts'] > round1_mean)]

# 2
df[df['draft_round'] == '1'].groupby('draft_year')['pts'].mean().plot()
