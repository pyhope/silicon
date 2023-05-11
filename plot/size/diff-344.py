
import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt
from scipy.optimize import curve_fit

fig, ax = plt.subplots(figsize=(8, 8))

def linear_func(x, m, c):
    return m * x + c

T = np.array([1400 + 50 * j for j in range(13)])
diff = np.array([-2509.41, -1778.5, -1389.79, -1193.46, -972.56, -222.74, 13.08, 255.88, 588.37, 1201.5, 1760.11, 1739.8, 2289.61])
popt, pcov = curve_fit(linear_func, T, diff)
m, c = popt
dm, dc = np.sqrt(np.diag(pcov))
x_intercept = -c / m
dx_intercept = np.sqrt((dc / m) ** 2 + (c * dm / m ** 2) ** 2)

print('slope = %.2f +/- %.2f; intercept = %.2f +/- %.2f; root = %.2f +/- %.2f' % (m, dm, c, dc, x_intercept, dx_intercept))
print(x_intercept, dx_intercept)

ax.scatter(T, diff, label='Data points')
ax.plot(T, linear_func(T, m, c), c='k', ls = '--', alpha = 0.5, label='Linear fitted data')
ax.axhline(y=0, c='k', ls = '-', alpha = 0.5)
ax.scatter(x_intercept, 0, c='k', label = '$T_m$ = %d $\pm$ %d K' % (x_intercept, dx_intercept))
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Free energy difference (kJ/mol)")

mpt.minor(ax)
mpt.legend()
mpt.savepdf('../diff-344')
#plt.show()