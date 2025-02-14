#!/bin/bash
#SBATCH --output=strong_input.dat
#SBATCH --nodes=1

python strong_scaling.py -nc 1 -nx 1000 -ny 10000 -nt 900

#SBATCH --output=strong_input.dat
#SBATCH --nodes=2

python strong_scaling.py -nc 2 -nx 1000 -ny 10000 -nt 900

#SBATCH --output=strong_input.dat
#SBATCH --nodes=4

python strong_scaling.py -nc 4 -nx 1000 -ny 10000 -nt 900

