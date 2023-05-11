import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt

fig, ax = plt.subplots(figsize=(8, 8))

N = np.array([216, 288, 384, 512, 1000])
x = 1/N

T = np.array([1720.1813226742906, 1707.238745, 1702.188272, 1691.1174566989523, 1677.4535057498272])
T_err = np.array([74.37760429, 101.6295485, 74.92014337, 68.40947379, 82.67894429837209])

ax.errorbar(x, T, yerr=T_err, ls='none', ecolor='k', elinewidth=1, capsize=4, capthick=1, zorder=0)
ax.scatter(x, T, marker='s', s=50, c='C0', edgecolors=(0.122, 0.467, 0.706, 0.6), linewidths=2, zorder=10, label='Data points')
pn, pn_err = mpt.fit(x, T, 1)
x_new = np.linspace(0, max(x), 100)
ax.plot(x_new, pn(x_new), c='k', ls='--', alpha=0.5, label='Linear fitted data')
ax.set_xlabel('$1/N$')
ax.set_ylabel('$T_m$ (K)')
ax.set_xlim(0, 0.005)
ax.set_ylim(1400, 2000)
ax.scatter(0, pn[0], c='k', label = '$T_\infty$ = %d K' % (pn[0]))
mpt.minor(ax)
mpt.legend()
print('(%.2f +/- %.2f), (%.2f +/- %.2f)' % (pn[1], pn_err[1], pn[0], pn_err[0]))
# (11360.21 +/- 338.08), (1667.87 +/- 1.00)
mpt.savepdf('../size')
plt.show()