import pandas as pd

df = pd.read_csv('Pokemon.csv')

# 1
df = df.drop_duplicates('#')

# 2
df['Type 2'] = df['Type 2'].replace(pd.NA, 'None')

# 3
df.to_csv('pm/all.csv')
df[df['Legendary']].to_csv('pm/legendary.csv')
df[~df['Legendary']].to_csv('pm/common.csv')
