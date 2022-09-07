import pandas as pd

df = pd.read_csv('titles.csv')
df[(df['age_certification'] == 'PG') & (df['imdb_votes'] >= 10000)]['release_year'].hist(color='black')
