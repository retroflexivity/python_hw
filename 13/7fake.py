import pandas as pd

df = pd.read_csv('nba.csv')
df.head()

round1_mean = df[df['draft_round'] == '1'].groupby('draft_year')['pts'].mean()
round1_mean

# 1
df = df[df['draft_year'].isin(round1_mean.index)]
df[(df['draft_round'] == '2') & (df['pts'] > round1_mean[df['draft_year']])]

# 2
round1_mean.plot()
