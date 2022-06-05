import pandas as pd

df = pd.read_csv('netflix.csv')

# 1
df[df['rating'] == 'G']

# 2
df[(df['listed_in'].str.find('Dramas') >= 0) & (df['release_year'] < 2017)]

# 3
df[df['type'] == 'Movie'].groupby(lambda x: 'old' if df.at[x, 'release_year'] < 1980 else 'new' if df.at[x, 'release_year'] >= 2019 else 'modern')['show_id'].count().idxmax()
