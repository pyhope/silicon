# The input files for MD simulation
## Only show the simulation at 1700 K with 216 atoms as an example
## Scripts are available in the github repo: https://github.com/pyhope/silicon
## Script 1: start.lmp

```
echo both

# Define some variables
variable	temperature equal 1700.
variable	tempDamp equal 0.1 # approx 0.1 ps
variable	pressure equal 1.
variable	pressureDamp equal 1.0
variable	seed equal 74581

# Setup
units		metal
atom_style	full

# Initial configuration
# Cubic diamond lattice
lattice 	diamond 5.4307
region          myreg block 0 3 0 3 0 3
create_box      1 myreg
create_atoms    1 region myreg
variable 	mass equal 28.0855
mass            1 ${mass}

# More setup options
variable	out_freq equal 500
variable	out_freq2 equal 500
neigh_modify    delay 10 every 1
pair_style 	sw
pair_coeff 	* * Si.sw Si
timestep	0.002
thermo          ${out_freq}
thermo_style 	custom step temp pe press lx
restart 	${out_freq} Restart.lmp Restart2.lmp

# Perform minimization
minimize 1.0e-2 1.0e-3 100 1000

reset_timestep 	0

# NVT equilibration

fix             1 all nve
fix             2 all temp/csvr ${temperature} ${temperature} ${tempDamp} ${seed}

velocity        all create ${temperature} ${seed} dist gaussian
run             25000

unfix           1
unfix           2

# NPT equilibration
# The symmetry of the crystal structure allows us to use an isotropic barostat

fix             1 all nph iso ${pressure} ${pressure} ${pressureDamp}
fix             2 all temp/csvr ${temperature} ${temperature} ${tempDamp} ${seed}

velocity        all create ${temperature} ${seed} dist gaussian
run             25000

unfix           1
unfix           2


# Dump trajectories in dump and dcd format
dump            myDump all atom ${out_freq2} si.lammps-dump-text
dump            myDcdDump all dcd ${out_freq2} out.dcd

# NPT + enhanced sampling

reset_timestep  0

fix             1 all plumed plumedfile plumed.dat outfile log.plumed
fix             2 all nph iso ${pressure} ${pressure} ${pressureDamp}
fix             3 all temp/csvr ${temperature} ${temperature} ${tempDamp} ${seed}
fix		4 all momentum 10000 linear 1 1 1 angular

run             5000000

unfix		4
unfix		3
unfix		2
unfix		1

write_data	data.final

```

## Script 2: plumed.dat

```
# vim:ft=plumed

ENVIRONMENTSIMILARITY ...
 SPECIES=1-216
 SIGMA=0.04
 LATTICE_CONSTANTS=0.5431 # in nm
 CRYSTAL_STRUCTURE=DIAMOND
 LABEL=es
 MORE_THAN={RATIONAL R_0=0.5 NN=6 MM=12}
 MEAN
... ENVIRONMENTSIMILARITY

METAD ...
 ARG=es.morethan
 SIGMA=3
 HEIGHT=60 # in kJ/mol
 PACE=500 # Every 500 steps is standard
 BIASFACTOR=50 # A barrier of 50 kT will be reduced to 1 kT once the bias is converged
 TEMP=1700 # Temperature in K
 LABEL=metad
... METAD

PRINT STRIDE=500  ARG=* FILE=COLVAR

```
