import pandas as pd
from seaborn import heatmap

df = pd.read_csv('Pokemon.csv')
df = df.drop_duplicates('#')
df.head()

# 1
df.groupby('Type 1')['HP'].mean().plot(kind='bar')

# 2
df.groupby('Generation')['#'].count().plot()
df.groupby('Generation')['HP'].agg('mean')

# 3
# я про разрез ничего не понял, но тут вроде нормально видно
heatmap(df.groupby(['Type 1', 'Type 2']).size().unstack())
