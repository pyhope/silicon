import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt

data=np.genfromtxt("./out.txt")
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(data[:,0],data[:,1])
ax.scatter(data[:,0],data[:,1])
ax.set_xlabel("SIGMA")
ax.set_ylabel("Overlap")
ax.axhline(0.0027414675, ls='--', c='k', alpha=0.5)
ax.scatter(0.067, 0.0027414675, c='k', label = 'Best SIGMA = 0.067')
# 0.067 0.0027414675
mpt.legend()
mpt.savepdf('../overlap')

plt.cla()
liquid = np.genfromtxt("./liquid/histo-0.067")
solid = np.genfromtxt("./solid/histo-0.067")
ax.plot(liquid[:,0], liquid[:,1], label ='Liquid')
ax.plot(solid[:,0], solid[:,1], label ='Solid')
# for index, i in enumerate(liquid[:,1] - solid[:,1]):
#     if np.isclose(i, 0.005335, rtol=1e-9):
#         print(index)
ax.set_xlim([0.4,1.3])
ax.axvline(liquid[586][0], ls='--', c='k', alpha = 0.5)
ax.set_xlabel('$k(\chi)$')
ax.set_ylabel('Probability density')
mpt.legend()
mpt.savepdf('../best_histo')