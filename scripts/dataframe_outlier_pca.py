import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    data = [[2,4,3,5,6,7,8,3,2],
            [1,5,7,4,2,4,6,4,4],
            [3,3,4,5,3,2,5,7,8],
            [4,8,9,5,8,2,3,4,6],
            [3,6,5,7,3,2,4,3,4],
            [12,14,15,21,32,12,19,15,10]],
    columns = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9'])

from sklearn.preprocessing import StandardScaler

features = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9']# Separating out the features
x = df.loc[:, features].values# Separating out the target
x = StandardScaler().fit_transform(x)

from sklearn.decomposition import PCA

pca = PCA(n_components = 2)
principal_components = pca.fit_transform(x)
principal_df = pd.DataFrame(data = principal_components, 
                           columns = ['Principal Component 1', 
                                      'Principal Component 2'])

fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (6, 6))

ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('Principal Component Analysis', fontsize = 18)

ax.scatter(principal_df.loc[:, 'Principal Component 1'],
           principal_df.loc[:, 'Principal Component 2'],
           s = 75)

ax.grid()