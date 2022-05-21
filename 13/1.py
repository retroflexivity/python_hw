import pandas as pd

ds = pd.read_csv('netflix.csv')
ds.head()
ds[ds['type'] == 'Movie'].to_csv('movies.csv')
ds[ds['type'] == 'TV Show'].to_csv('shows.csv')
ds[ds['listed_in'].str.find('Dramas') >= 0].to_csv('dramas.csv')
