import pandas as pd
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"# load dataset into Pandas DataFrame
df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target'])

from sklearn.preprocessing import StandardScaler

features = ['sepal length', 'sepal width', 'petal length', 'petal width']# Separating out the features
x = df.loc[:, features].values# Separating out the target
y = df.loc[:,['target']].values# Standardizing the features
x = StandardScaler().fit_transform(x)

from sklearn.decomposition import PCA

pca = PCA(n_components = 2)
principal_components = pca.fit_transform(x)
principal_df = pd.DataFrame(data = principal_components, 
                           columns = ['Principal Component 1', 'Principal Component 2'])

final_df = pd.concat([principal_df, df[['target']]], axis = 1)

fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (6, 6))

ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('Principal Component Analysis', fontsize = 20)

targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['red', 'green', 'blue']

for target, color in zip(targets,colors):
    indices_to_keep = (final_df['target'] == target)
    ax.scatter(final_df.loc[indices_to_keep, 'Principal Component 1'], 
               final_df.loc[indices_to_keep, 'Principal Component 2'], 
               c = color, 
               s = 75)
ax.legend(targets, frameon = False, title = 'Species', bbox_to_anchor = (1.0, 1.0))
ax.grid()