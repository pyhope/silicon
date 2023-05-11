import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt

fig = plt.figure(figsize=(12, 16))
gs = fig.add_gridspec(4, 3, wspace=0.04, hspace=0.1)
axes = gs.subplots(sharex=True, sharey=True)

sigma = [np.round(0.025 + 0.005 * j, 3) for j in range(12)]
sigma_2D = np.array(sigma).reshape((4, 3))
Liquid = dict()
Solid = dict()

for i in sigma:
    Solid[i] = np.genfromtxt("solid/histo-%.3f" % (i))
    Liquid[i] = np.genfromtxt("liquid/histo-%.3f" % (i))

for i, _ in enumerate(sigma_2D):
    for j, value in enumerate(_):
        solid, liquid, ax = Solid[value], Liquid[value], axes[i,j]
        ax.plot(liquid[:,0], liquid[:,1], label ='Liquid')
        ax.plot(solid[:,0], solid[:,1], label ='Solid')
        ax.set_xlim([-0.1,1.5])
        ax.set_title("Sigma = " + str(value) + " nm", fontsize = 14)
        ax.legend(fancybox=False, edgecolor='black', fontsize = 14, loc = 'upper left') 

for ax in axes[-1, :]:
    ax.set_xlabel('$k(\chi)$')
for ax in axes[:, 0]:
    ax.set_ylabel('Probability density')
mpt.savepdf('../histo')