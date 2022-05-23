import pandas as pd


def fix_dur(df):
    df['duration'] = df['duration'].map(lambda x: int(str(x).split()[0]) if x == x else 0)


df = pd.read_csv('netflix.csv')

mv = df[df['type'] == 'Movie'].copy()
fix_dur(mv)
mv.groupby('release_year')['duration'].mean().plot(xlabel='release year', ylabel='duration')

sr = df[df['type'] == 'TV Show'].copy()
fix_dur(sr)
sr.groupby('country')['duration'].sum().sort_values(ascending=False).reset_index()

dm = df[df['listed_in'].str.find('Dramas') >= 0]
dm.groupby('release_year')['show_id'].count()
