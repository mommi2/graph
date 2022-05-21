from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)
k = 5
mean, var, skew, kurt = gamma.stats(k, moments='mvsk')
x = np.linspace(0, 10, 100)
print(gamma.pdf(x + 1, k))
ax.plot(x, gamma.pdf(x + 1, k), 'r-', lw=5, alpha=0.6, label='gamma pdf')
plt.show()