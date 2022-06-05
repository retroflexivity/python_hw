import pandas as pd
import matplotlib as plt

df = pd.read_csv('iris.csv')
df[df['species'] == 'setosa'].sepal_width.hist(legend=True, alpha=0.5)
df[df['species'] == 'versicolor'].sepal_width.hist(legend=True, alpha=0.5)
df[df['species'] == 'virginica'].sepal_width.hist(legend=True, alpha=0.5)
plt.legend(['setosa', 'versicolor', 'virginica'])
plt.xlabel('sepal width')
plt.ylabel('count')
