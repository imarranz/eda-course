import pandas as pd
import numpy as np
import scipy as sp
from scipy.stats import probplot
import matplotlib.pyplot as plt
import seaborn as sns

def mahalanobis(x = None, data = None, cov = None):
    """Compute the Mahalanobis Distance between each row of x and the data  
    x    : vector or matrix of data with, say, p columns.
    data : ndarray of the distribution from which Mahalanobis distance of each observation of x is to be computed.
    cov  : covariance matrix (p x p) of the distribution. If None, will be computed from data.
    """
    x_minus_mu = x - np.mean(data)
    if not cov:
        cov = np.cov(data.values.T)
    inv_covmat = np.linalg.inv(cov)
    left_term = np.dot(x_minus_mu, inv_covmat)
    mahal = np.dot(left_term, x_minus_mu.T)
    return mahal.diagonal()


mean = (1,2)
cov = [[0.22,0.19],[0.19,0.22]]
np.random.seed(1)
x = np.random.multivariate_normal(mean, cov, 150)

fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, figsize = (17, 5))

X = pd.concat([pd.DataFrame(x, columns = list('AB')), pd.DataFrame({'A': [0.25], 'B': [3.25]})], axis = 0)
X.plot(kind = 'scatter', x = 'A', y = 'B', ax = ax1)
ax1.scatter(x = X.mean()[0], y = X.mean()[1], color = 'orange', marker = '+', s = 300)     
ax1.plot([0.25], [3.25], 'ro')
ax1.text(0.30, 3.25, 'Outiler', color = 'red')
ax1.set_xlabel('Variable A')
ax1.set_ylabel('Variable B')

sns.distplot(mahalanobis(x = X, data = X), hist = False, rug = True, kde = True, kde_kws = {'linewidth': 3}, rug_kws = {'color': 'black'}, ax = ax2)
ax2.text(44.5, 0.03, 'Outlier', color = 'red')

probplot(mahalanobis(x = X, data = X), dist = "chi", sparams = (1,), plot = ax3)

for ax in [ax1, ax2, ax3]:
    ax.grid(True, linestyle = '--', color = 'gray', alpha = 0.5)

plt.show()