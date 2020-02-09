import pandas as pd
from numpy.random import randint, seed
from numpy import nan
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression

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

y = df.loc[~df.index.isin(samples), 'petal length (cm)'].values
X = df.loc[~df.index.isin(samples), 'petal width (cm)'].values
X = X.reshape(-1,1)
y = y.reshape(-1,1)
reg = LinearRegression().fit(X, y)

X_new = df.loc[df.index.isin(samples), 'petal width (cm)'].values
X_new = X_new.reshape(-1,1)

#df.loc[samples, 'petal length (cm)'] = reg.predict(X_new).reshape(-1)

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (15, 5))

ax1.scatter(df['petal length (cm)'], df_original['petal length (cm)'], c = colores,)

ax1.scatter(reg.predict(X_new).reshape(-1), 
            df_original.loc[df_original.index.isin(samples), 'petal length (cm)'])

ax1.set_xlabel('petal length (cm)')
ax1.set_ylabel('petal length (cm)\nOriginal data')

ax2.scatter(df['petal length (cm)'], df_original['petal width (cm)'], c = colores, )

ax2.scatter(reg.predict(X_new).reshape(-1), 
            df_original.loc[df_original.index.isin(samples), 'petal width (cm)'])

ax2.set_xlabel('petal length (cm)')
ax2.set_ylabel('petal width (cm)')

plt.show()