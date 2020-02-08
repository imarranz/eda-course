# LIBRERÍAS ---------------------------------------------------------------

from numpy.random import normal, exponential, logistic, chisquare
import scipy.stats as stats
import matplotlib.pyplot as plt

# NÚMERO DE OBSERVACIONES -------------------------------------------------

N = 150

# REPRESENTACIÓN GRÁFICA --------------------------------------------------

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows = 2, ncols = 3, figsize = (15, 7))

measurements = normal(loc = 20, scale = 5, size = N)   
stats.probplot(measurements, dist = "norm", plot = ax1)
ax4.hist(measurements, rwidth = 0.8)

measurements = exponential(scale = 5, size = N)   
stats.probplot(measurements, dist = "norm", plot = ax2)
ax5.hist(measurements, rwidth = 0.8)

measurements = chisquare(df = 3, size = N)   
stats.probplot(measurements, dist = "norm", plot = ax3)
ax6.hist(measurements, rwidth = 0.8)

ax1.set_title('Probability Plot\nNormal Distribution')
ax2.set_title('Probability Plot\nExponential Distribution')
ax3.set_title('Probability Plot\n$\chi^{2}_{3}$ Distribution')

for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    ax.grid(linestyle = '--', color = 'gray', alpha = 0.4)

plt.show()