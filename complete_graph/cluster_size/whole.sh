#!/bin/bash

nrun=$1
ns=$2

for ((i=0; i<$ns; i++))
	do
		echo $i
		./solitary_ABM_error 100 8 $nrun > ./N100_L8_dat/N100_L8_image_s$i
	done
