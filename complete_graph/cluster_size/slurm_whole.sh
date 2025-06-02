#!/bin/bash

ns=$1
for ((i=0; i<$ns; i++))
	do
		sbatch run.sh $i
	done
