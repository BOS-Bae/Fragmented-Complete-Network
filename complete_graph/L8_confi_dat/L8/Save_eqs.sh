#!/bin/bash
Ni=$1
Nf=$2

for ((m=$Ni; m<=$Nf; m++))
do
	for ((n=$Ni; n<=$Nf; n++))
	do
		python3 show_eq.py $m $n > ./eqs_dat/L8-m$m-n$n-eqs.dat
	done
done
