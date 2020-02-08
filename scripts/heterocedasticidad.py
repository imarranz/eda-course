import pandas as pd
import numpy as np
from numpy.random import normal
import scipy.stats as stats
from scipy.stats import probplot
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'Groups': list('A'*50+'B'*50+'C'*50),
    'Values': np.concatenate([normal(loc = 0, scale = 1, size = 50), 
               normal(loc = 1, scale = 3, size = 50), 
               normal(loc = 3, scale = 6, size = 50)])})

fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, figsize = (15,5))

sns.boxplot(x = 'Groups', y = 'Values', data = data, ax = ax1)

y = data.Values.values
y = y.reshape(-1,1)
X = np.repeat([0,1,2], 50)
X = X.reshape(-1,1)

reg = LinearRegression().fit(X, y)
residuos = (y - reg.predict(X))
pd.DataFrame({'x': np.linspace(1,50), 'y': residuos[:50].reshape(-1)})\
    .plot(kind = 'scatter', x = 'x', y = 'y', marker = 'o', s = 50,
          linewidth = 0, legend = False, ax = ax2, color = 'C0')
pd.DataFrame({'x': np.linspace(51,100), 'y': residuos[50:100].reshape(-1)})\
    .plot(kind = 'scatter', x = 'x', y = 'y', marker = 'o', s = 50,
          linewidth = 0, legend = False, ax = ax2, color = 'C1')
pd.DataFrame({'x': np.linspace(101,150), 'y': residuos[100:150].reshape(-1)})\
    .plot(kind = 'scatter', x = 'x', y = 'y', marker = 'o', s = 50,
          linewidth = 0, legend = False, ax = ax2, color = 'C2')

ax2.set_xlabel(r'Samples')
ax2.set_ylabel('$y - \hat{y}$')

ax2.axhline(0, linestyle = '--', color = 'gray')

(osm, osr), (slope, intercept, r ) = probplot(residuos.reshape(-1)[:50], dist = "norm", plot = None, )
ax3.scatter(osm, osr, color = 'C0')
x_vals = np.linspace(-2, 2, 100)
y_vals = intercept + slope * x_vals
ax3.plot(x_vals, y_vals, '--', color = 'C0')
ax3.grid(True, linestyle = '--', color = 'gray', alpha = 0.5)

(osm, osr), (slope, intercept, r ) = probplot(residuos.reshape(-1)[50:100], dist = "norm", plot = None, )
ax3.scatter(osm, osr, color = 'C1')
x_vals = np.linspace(-2, 2, 100)
y_vals = intercept + slope * x_vals
ax3.plot(x_vals, y_vals, '--', color = 'C1')

(osm, osr), (slope, intercept, r ) = probplot(residuos.reshape(-1)[100:150], dist = "norm", plot = None, )
ax3.scatter(osm, osr, color = 'C2')
x_vals = np.linspace(-2, 2, 100)
y_vals = intercept + slope * x_vals
ax3.plot(x_vals, y_vals, '--', color = 'C2')

plt.show()