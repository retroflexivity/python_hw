import pandas as pd

df = pd.read_csv('netflix.csv')

df['date_added'] = pd.to_datetime(df['date_added'])
df[df['type'] == 'Movie'].groupby(lambda x: df.at[x, 'date_added'].month)['show_id'].count().idxmax()
int(df[df['type'] == 'TV Show'].groupby(lambda x: df.at[x, 'date_added'].month)['show_id'].count().idxmax())
# я не понимаю почему но без int() там флот
