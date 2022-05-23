import pandas as pd

df = pd.read_csv('netflix.csv')
df[df['type'] == 'Movie'].to_csv('nf/movies.csv')
df[df['type'] == 'TV Show'].to_csv('nf/shows.csv')
df[df['listed_in'].str.find('Dramas') >= 0].to_csv('nf/dramas.csv')

df.head()
