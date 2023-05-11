import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt

fig = plt.figure(figsize=(12, 16))
gs = fig.add_gridspec(4, 3, wspace=0, hspace=0)
axes = gs.subplots(sharex=True, sharey=True)

T = [1450 + 50 * j for j in range(12)]
T_2D = np.array(T).reshape((4, 3))
Data = dict()

for i in T:
    Data[i] = np.genfromtxt("data/" + str(i) + ".dat")
for i, _ in enumerate(T_2D):
    for j, value in enumerate(_):
        fes, ax = Data[value], axes[i,j]
        N = fes.shape[0]
        ax.plot(fes[:,0], fes[:,1], label = str(value) + ' K')
        freeEnergyLiquid = np.amin(fes[:,1][:int(N/2)])
        freeEnergySolid = np.amin(fes[:,1][int(N/2):])
        print(value, freeEnergySolid-freeEnergyLiquid)
        ax.axhline(y = freeEnergyLiquid, c='k', ls='-', alpha=0.5, label = 'Liquid')
        ax.axhline(y = freeEnergySolid, c='k', ls='--', alpha=0.5, label = 'Solid')
        mpt.minor(ax)
        ax.legend(fancybox=False, edgecolor='black', fontsize = 14, loc = 'upper center')    

for ax in axes[-1, :]:
    ax.set_xlabel('Collective variable')
for ax in axes[:, 0]:
    ax.set_ylabel('Free energy (kJ/mol)')

mpt.savepdf('../fes')
# plt.show()
