import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt
from scipy.optimize import curve_fit

fig, ax = plt.subplots(figsize=(8, 8))

def linear_func(x, m, c):
    return m * x + c

T = np.array([1450 + 50 * j for j in range(12)])
diff = np.array([-3729.64, -3105.57, -2337.05, -2043.44, -271.83, 226.34, 1807.71, 2219.56, 2656.85, 3637.73, 5227.62, 5896.76])
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
mpt.savepdf('../diff-555')
#plt.show()