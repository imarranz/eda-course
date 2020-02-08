import matplotlib.pyplot as plt
from numpy.random import normal
from scipy.stats import shapiro
from IPython.display import display, Markdown

x = normal(loc = 2, scale = 1, size = 100)
x = x**2

plt.hist(x, rwidth = 0.8)
plt.show()
w, p = shapiro(x)
display(Markdown("W: {:.2f}\t statistic: {:.4f}".format(w,p)))