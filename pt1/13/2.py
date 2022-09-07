import pandas as pd


def fix_dur(df):
    df['duration'] = df['duration'].map(lambda x: int(str(x).split()[0]) if x == x else 0)


df = pd.read_csv('netflix.csv')
mv = df[df['type'] == 'Movie'].copy()
sr = df[df['type'] == 'TV Show'].copy()
dm = df[df['listed_in'].str.find('Dramas') >= 0]

# 1
fix_dur(mv)
fix_dur(sr)

# 2
mv.groupby('release_year')['duration'].mean().plot(xlabel='release year', ylabel='duration')

# 3
sr.groupby('country')['duration'].sum().sort_values(ascending=False).reset_index()

# 4
dm.groupby('release_year')['show_id'].count()
