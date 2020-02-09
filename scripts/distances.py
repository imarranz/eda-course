# LIBRERÍAS ---------------------------------------------------------------

import numpy as np
from numpy.random import normal
from scipy.spatial.distance import mahalanobis, euclidean
import matplotlib.pyplot as plt

# GENERAMOS VARIABLES ALEATORIAS ------------------------------------------

np.random.seed(0)
N = 150
A = normal(loc = 0.0, scale = 0.8, size = N)
B = normal(loc = 0.0, scale = 3.0, size = N)

# MATRIZ DE COVARIANZAS ---------------------------------------------------

np.cov(A,B)

# INVERSA DE LA MATRIZ DE COVARIANZAS -------------------------------------

np.linalg.inv(np.cov(A,B))

# REPRESENTACIÓN GRÁFICA --------------------------------------------------

fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (6,6))
ax.scatter(A, B, alpha = 0.75)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True, linestyle = '--', color = 'gray', alpha = 0.5)
ax.plot([0,0], [1, 6], color = 'red', linewidth = 2, marker = 'o', markersize = 10)
ax.plot([0,2], [0, 0], color = 'green', linewidth = 2, marker = 'o', markersize = 10)
ax.set_xticks(range(-10, 12, 2))
ax.set_yticks(range(-10, 12, 2))
ax.set_xlabel(r'Variable B', fontsize = 12)
ax.set_ylabel(r'Variable A', fontsize = 12)
plt.show()