#!/bin/bash
#SBATCH --job-name=liquid        # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=6              # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --time=00:59:00          # total run time limit (HH:MM:SS)
#SBATCH --constraint=cascade

module purge
module load intel/2021.1.2
module load intel-mpi/intel/2021.1.1
module load anaconda3/2021.5
module load fftw/intel-2021.1/intel-mpi/3.3.9

srun lmp_della_new -in start.lmp