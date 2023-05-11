import numpy as np
import lammps_logfile as log
from matplotlib import pyplot as plt
import my_pyplot as mpt

Data = dict()
Data['Liquid'] = log.File('liq.lammps')
Data['Solid'] = log.File('sol.lammps')

fig, ax = plt.subplots(2, 1, figsize=(8,12), sharex=True)
fig.subplots_adjust(hspace=0)

for phase in ('Liquid', 'Solid'):
    for index, i in enumerate(["Volume", "Enthalpy"]):
        x = Data[phase].get("Step") * 0.002
        y = Data[phase].get(i)/216
        avgy = np.mean(y)
        stdy = np.std(y)
        ax[index].plot(x, y, lw=0.5, label=phase + ': ' + '%.2f $\pm$ %.2f' % (avgy, stdy))
        ax[index].axhline(avgy, c = 'k', ls = '--', alpha = 0.5)
        ax[index].legend(fancybox=False, edgecolor='black')
        #ax[index].text(100, avgy, phase , c='white')
        mpt.minor(ax[index])
        #ax[index].set_title(i + ' = ' + "%.2f" % (avgy))
ax[0].set_ylabel("Volume (Å$^3$/atom)")
ax[1].set_ylabel("Enthalpy (eV/atom)")
ax[1].set_xlabel('Time (ps)')

latentheat = (Data['Liquid'].get('Enthalpy') - Data['Solid'].get('Enthalpy'))/216
volume_s = Data['Solid'].get('Volume')/216 * 1.8897259886**3
volume_l = Data['Liquid'].get('Volume')/216 * 1.8897259886**3
DeltaV = volume_l - volume_s
DeltaVoverVs = DeltaV / volume_s
print('Latent heat is %.2f +- %.2f' % (np.mean(latentheat), np.std(latentheat)))
print('Specific volume of solid is %.2f +- %.2f' % (np.mean(volume_s), np.std(volume_s)))
print('Specific volume of liquid is %.2f +- %.2f' % (np.mean(volume_l), np.std(volume_l)))
print('Delta V is %.2f +- %.2f' % (np.mean(DeltaV), np.std(DeltaV)))
print('Delta V / V s is %.4f +- %.4f' % (np.mean(DeltaVoverVs), np.std(DeltaVoverVs)))
mpt.savepdf('../props')

'''
Latent heat is 0.33 +- 0.16
Specific volume of solid is 137.34 +- 1.00
Specific volume of liquid is 127.51 +- 1.07
Delta V is -9.83 +- 1.45
Delta V / V s is -0.0716 +- 0.0102
'''