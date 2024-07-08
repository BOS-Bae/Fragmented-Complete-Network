#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1      # Cores per node
#SBATCH --partition=g5        # Partition Name
##
#SBATCH --job-name=prob_ABM
##SBATCH --time=24:00:00           # Runtime: HH:MM:SS
#SBATCH -o error_output/test.%N.%j.out         # STDOUT
#SBATCH -e error_output/test.%N.%j.err         # STDERR
##

hostname
date

cd $SLURM_SUBMIT_DIR

./run_frag.sh $1 30 1000000
