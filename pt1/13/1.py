import pandas as pd

df = pd.read_csv('netflix.csv')

# 1
df[df['type'] == 'Movie'].to_csv('nf/movies.csv')
# 2
df[df['type'] == 'TV Show'].to_csv('nf/shows.csv')
# 3
df[df['listed_in'].str.find('Dramas') >= 0].to_csv('nf/dramas.csv')
