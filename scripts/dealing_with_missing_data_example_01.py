import pandas as pd
from numpy.random import randint, seed
from numpy import nan
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

seed(19)
samples = randint(low = 0, high = 150, size = 25)
colores = ['C0' if x in samples else 'C1' for x in range(0,150)]

data = load_iris(return_X_y = False)

df = pd.DataFrame(data.data, columns = data.feature_names)
df['Species'] = data.target
df['Species'].replace({0: data.target_names[0], 
                       1: data.target_names[1], 
                       2: data.target_names[2]}, inplace = True)
df_original = df.copy()


df.loc[samples, 'petal length (cm)'] = nan

df.loc[samples, 'petal length (cm)'] = df['petal length (cm)'].mean()

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (15, 5))

ax1.scatter(df['petal length (cm)'], df_original['petal length (cm)'], c = colores)
ax1.set_xlabel('petal length (cm)')
ax1.set_ylabel('petal length (cm)\nOriginal data')
ax2.scatter(df['petal length (cm)'], df_original['petal width (cm)'], c = colores)
ax2.set_xlabel('petal length (cm)')
ax2.set_ylabel('petal width (cm)')

plt.show()