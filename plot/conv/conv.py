import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt

fig, ax = plt.subplots(figsize=(10, 8))

for i in range(4):
    fes=np.genfromtxt("fes/fes_" + str(i) + ".dat")
    ax.plot(fes[:,0],fes[:,1],label=str((i+1)*0.25) + " ns")

for i in [1, 3]:
    fes=np.genfromtxt("fes/fes_" + str(i) + "0.dat")
    ax.plot(fes[:,0],fes[:,1],label=str((i+1)*2.5) + " ns")

ax.set_xlabel("Collective variable")
ax.set_ylabel("Free energy (kJ/mol)")
#ax.set_xlim([0,216])
mpt.minor(ax)
plt.legend(ncol = 2, fancybox=False, edgecolor='black')
mpt.savepdf('../conv')
# T = 1700 K, t = 10 ns