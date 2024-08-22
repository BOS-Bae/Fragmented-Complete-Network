#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1      # Cores per node
#SBATCH --partition=g4,g5        # Partition Name
##
#SBATCH --job-name=L8_c_dist
##SBATCH --time=24:00:00           # Runtime: HH:MM:SS
#SBATCH -o error_output/test.%N.%j.out         # STDOUT
#SBATCH -e error_output/test.%N.%j.err         # STDERR
##

hostname
date

cd $SLURM_SUBMIT_DIR

./ABM 100 8 > N100_L8_image_s$1
