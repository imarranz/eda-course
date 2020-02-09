import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import normal

X1 = normal(loc = 1, scale = 1, size = 100)
X2 = normal(loc = 1, scale = 1, size = 100)**2

df_boxplot = pd.DataFrame({'X1': X1, 'X2': X2})

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (12, 5))

df_boxplot['X1'].plot(kind = 'box', ax = ax1)
df_boxplot['X2'].plot(kind = 'box', ax = ax2)

ax1.set_xlim(0.9,1.1)
ax2.set_xlim(0.9,1.1)
ax1.set_title('Distribución Simétrica', fontsize = 16)
ax2.set_title('Distribución Asimétrica', fontsize = 16)

plt.show()